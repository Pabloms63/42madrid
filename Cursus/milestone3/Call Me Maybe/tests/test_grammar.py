"""Check that the grammar accepts every valid call and nothing else.

The cases below are written by hand, so they run against a fixed set of
functions kept in ``tests/fixtures`` rather than against the input file,
which may change.  Portability over the real data is covered by
``tests/test_real_data.py``.
"""

import json
import tempfile
from pathlib import Path
from typing import Dict, List, Optional

from src.decoder import Decoder
from src.grammar import Grammar, GrammarError
from src.loader import load_functions
from src.parser import parse_call

ROOT = Path(__file__).resolve().parent
functions = load_functions(ROOT / "fixtures" / "functions_definition.json")
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
    '{"name": "fn_is_even", "parameters": {"n": -7}}',
]
bad = [
    '{"name": "fn_unknown", "parameters": {}}',
    '{"name": "fn_add_numbers", "parameters": {"a": 01, "b": 3}}',
    '{"name": "fn_add_numbers", "parameters": {"a": 2.}}',
    '{"name": "fn_add_numbers", "parameters": {"a": 2, "b": "3"}}',
    '{"name": "fn_greet", "parameters": {"name": "un\nescaped"}}',
    '{"name": "fn_greet", "parameters": {"name": "x"}}}',
    '{"name": "fn_is_even", "parameters": {"n": 2.5}}',
    '{"name": "fn_is_even", "parameters": {"n": 1e3}}',
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
with tempfile.NamedTemporaryFile(
    "w", suffix=".json", delete=False, encoding="utf-8"
) as handle:
    handle.write(json.dumps(one))
empty = Grammar(load_functions(Path(handle.name)))
print("empty params forced:", repr(empty.start().forced_text()))
assert empty.start().advance(
    '{"name": "fn_now", "parameters": {}}').is_complete()


# 7. drive the decoder with a fake model instead of the real one
class FakeModel:
    """A language model whose logits are decided in advance."""

    def __init__(self, plan: List[List[float]]) -> None:
        """Store the scores to return, one list per forward pass."""
        self.plan = plan
        self.calls = 0

    def encode(self, text: str) -> List[int]:
        """Return a constant id: the fake model ignores its input."""
        return [1]

    def logits(self, input_ids: List[int]) -> List[float]:
        """Return the next planned scores, repeating the last one."""
        self.calls += 1
        return self.plan[min(self.calls - 1, len(self.plan) - 1)]


class FakeVocab:
    """A vocabulary of a few dozen hand-picked pieces."""

    def __init__(self, pieces: List[str]) -> None:
        """Number the pieces so they can be addressed like token ids."""
        self.pieces: Dict[int, str] = dict(enumerate(pieces))

    def text(self, token_id: int) -> Optional[str]:
        """Return the text produced by ``token_id``, if any."""
        return self.pieces.get(token_id)

    def ids(self) -> List[int]:
        """Return every known token id."""
        return list(self.pieces)


pieces = ['"', "{", "}", ",", " ", ":", "fn", "_", "add", "numbers", "greet",
          "shrek", "1", "2", "3", "0", ".", "hello", "reverse", "string",
          "get", "square", "root", "substitute", "with", "regex", "s", "a",
          "b", "name", "parameters", "source", "replacement", "\\", "d", "+",
          "N", "16", "144", "world", "e", "-"]


def prefer(*names: str) -> List[float]:
    """Return scores ranking ``names`` first, in the given order."""
    scores = [0.0] * len(pieces)
    for rank, name in enumerate(names):
        scores[pieces.index(name)] = 10.0 - rank
    return scores


# the model wants: fn_greet, then the value "shrek", then close the string
vocab = FakeVocab(pieces)
model = FakeModel([prefer("greet"), prefer("shrek"), prefer('"')])
decoder = Decoder(model, vocab, grammar)
out = decoder.decode("irrelevant")
print("decoded:", out, "in", decoder.forwards, "forwards")
print(parse_call("p", out, functions))
