import json
from pathlib import Path

from src.decoder import Decoder
from src.grammar import Grammar, GrammarError
from src.loader import load_functions
from src.parser import parse_call

functions = load_functions(Path("/mnt/project/functions_definition.json"))
grammar = Grammar(functions)

# 1. every template is valid JSON matching its own definition
for fn, parts in zip(functions, grammar.templates):
    print(repr("".join(p if isinstance(p, str) else "<%s>" % type(p).__name__
                       for p in parts)))

# 2. forced prefix
print("forced start:", repr(grammar.start().forced_text()))

# 3. accept / reject whole strings
good = [
    '{"name": "fn_add_numbers", "parameters": {"a": 2, "b": 3}}',
    '{"name": "fn_add_numbers", "parameters": {"a": -1.5e10, "b": 0}}',
    '{"name": "fn_greet", "parameters": {"name": "shrek"}}',
    '{"name": "fn_reverse_string", "parameters": {"s": "he\\"llo"}}',
    '{"name": "fn_substitute_string_with_regex", "parameters": '
    '{"source_string": "a", "regex": "\\\\d+", "replacement": "N"}}',
]
bad = [
    '{"name": "fn_unknown", "parameters": {}}',
    '{"name": "fn_add_numbers", "parameters": {"a": 01, "b": 3}}',
    '{"name": "fn_add_numbers", "parameters": {"a": 2.}}',
    '{"name": "fn_add_numbers", "parameters": {"a": 2, "b": "3"}}',
    '{"name": "fn_greet", "parameters": {"name": "un\nescaped"}}',
    '{"name": "fn_greet", "parameters": {"name": "x"}}}',
]
for text in good:
    state = grammar.start().advance(text)
    assert state.is_complete(), text
    call = parse_call("p", text, functions)
    print("OK  ", call.name, call.parameters)
for text in bad:
    try:
        state = grammar.start().advance(text)
        assert not state.is_complete(), "SHOULD HAVE BEEN REJECTED: %r" % text
        print("incomplete (ok)", text[:40])
    except GrammarError:
        print("rejected (ok) ", text[:40])

# 4. multi-character tokens crossing part boundaries
state = grammar.start().advance('{"name": "fn_greet", "parameters": {"name":')
assert state.accepts(' "shrek"}}')
assert state.accepts(' "')
assert not state.accepts(' 3')
print("boundary tokens ok")

# 5. numbers close on the delimiter, not before
state = grammar.start().advance(
    '{"name": "fn_get_square_root", "parameters": {"a": 16'
    )
assert state.accepts("}}"), "number must be able to end"
assert state.accepts("4"), "number must be able to grow"
assert state.accepts("}"), "a single brace is a valid prefix of }}"
assert not state.accepts("}}}"), "one brace too many"
print("number delimiter ok")

# 6. no-parameter function
one = json.loads('[{"name": "fn_now", "description": "d", "parameters": {},'
                 ' "returns": {"type": "string"}}]')
Path("/tmp/one.json").write_text(json.dumps(one))
empty = Grammar(load_functions(Path("/tmp/one.json")))
print("empty params forced:", repr(empty.start().forced_text()))
assert empty.start().advance(
    '{"name": "fn_now", "parameters": {}}').is_complete()


# 7. drive the decoder with a fake model that always prefers 'z'
class FakeModel:
    def __init__(self, plan: list[list[float]]) -> None:
        self.plan = plan
        self.calls = 0

    def encode(self, text: str) -> list[int]:
        return [1]

    def logits(self, input_ids: list[int]) -> list[float]:
        self.calls += 1
        return self.plan[min(self.calls - 1, len(self.plan) - 1)]


class FakeVocab:
    def __init__(self, pieces: list[str]) -> None:
        self.pieces = dict(enumerate(pieces))

    def text(self, token_id: int) -> str | None:
        return self.pieces.get(token_id)

    def ids(self) -> list[int]:
        return list(self.pieces)


pieces = ['"', "{", "}", ",", " ", ":", "fn", "_", "add", "numbers", "greet",
          "shrek", "1", "2", "3", "0", ".", "hello", "reverse", "string",
          "get", "square", "root", "substitute", "with", "regex", "s", "a",
          "b", "name", "parameters", "source", "replacement", "\\", "d", "+",
          "N", "16", "144", "world", "e", "-"]

vocab = FakeVocab(pieces)
model = FakeModel(vocab)
model.calls = 0


def prefer(*names):
    scores = [0.0] * len(pieces)
    for rank, name in enumerate(names):
        scores[pieces.index(name)] = 10.0 - rank
    return scores


# the model wants: fn_greet, then the value "shrek", then close the string
model.plan = [prefer("greet"), prefer("shrek"), prefer('"')]
decoder = Decoder(model, vocab, grammar)
out = decoder.decode("irrelevant")
print("decoded:", out, "in", decoder.forwards, "forwards")
print(parse_call("p", out, functions))
