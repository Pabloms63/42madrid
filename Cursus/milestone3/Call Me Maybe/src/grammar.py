import json
from typing import Dict, List, Optional, Sequence, Set, Tuple, Union

from .models import FunctionDefinition

DIGITS = frozenset("0123456789")
HEXDIGITS = frozenset("0123456789abcdefABCDEF")
ESCAPES = frozenset('"\\/bfnrt')

Cursor = Tuple[int, int, Union[int, str]]


class GrammarError(Exception):
    """Raised when a grammar cannot be built or no longer accepts the text."""


class ValueAutomaton:
    initial: str = ""

    def step(self, state: str, char: str) -> List[str]:
        raise NotImplementedError

    def is_final(self, state: str) -> bool:
        raise NotImplementedError

    def next_chars(self, state: str) -> Optional[Set[str]]:
        raise NotImplementedError


class NumberAutomaton(ValueAutomaton):
    initial = "start"
    ALPHABET = "-+.eE0123456789"
    FINAL = frozenset({"zero", "integer", "fraction", "exponent_digit"})

    def step(self, state: str, char: str) -> List[str]:
        if state == "start":
            if char == "-":
                return ["sign"]
            if char == "0":
                return ["zero"]
            if char in "123456789":
                return ["integer"]
        elif state == "sign":
            if char == "0":
                return ["zero"]
            if char in "123456789":
                return ["integer"]
        elif state == "zero":
            if char == ".":
                return ["point"]
            if char in "eE":
                return ["exponent"]
        elif state == "integer":
            if char in DIGITS:
                return ["integer"]
            if char == ".":
                return ["point"]
            if char in "eE":
                return ["exponent"]
        elif state == "point":
            if char in DIGITS:
                return ["fraction"]
        elif state == "fraction":
            if char in DIGITS:
                return ["fraction"]
            if char in "eE":
                return ["exponent"]
        elif state == "exponent":
            if char in "+-":
                return ["exponent_sign"]
            if char in DIGITS:
                return ["exponent_digit"]
        elif state == "exponent_sign":
            if char in DIGITS:
                return ["exponent_digit"]
        elif state == "exponent_digit":
            if char in DIGITS:
                return ["exponent_digit"]
        return []

    def is_final(self, state: str) -> bool:
        return state in self.FINAL

    def next_chars(self, state: str) -> Optional[Set[str]]:
        return {char for char in self.ALPHABET if self.step(state, char)}


class IntegerAutomaton(NumberAutomaton):
    ALPHABET = "-0123456789"
    FINAL = frozenset({"zero", "integer"})

    def step(self, state: str, char: str) -> List[str]:
        if char in ".eE":
            return []
        return super().step(state, char)


class StringAutomaton(ValueAutomaton):
    """Recognise a quoted JSON string, escapes included."""

    initial = "start"
    HEX_CHAIN = {
        "hex1": "hex2", "hex2": "hex3", "hex3": "hex4", "hex4": "body"
        }
    BODY = frozenset({"first", "body"})

    def step(self, state: str, char: str) -> List[str]:
        if state == "start":
            return ["first"] if char == '"' else []
        if state in self.BODY:
            if char == '"':
                return ["done"]
            if char == "\\":
                return ["escape"]
            if char == " " and state == "first":
                return []
            return ["body"] if char >= " " else []
        if state == "escape":
            if char in ESCAPES:
                return ["body"]
            return ["hex1"] if char == "u" else []
        if state in self.HEX_CHAIN:
            return [self.HEX_CHAIN[state]] if char in HEXDIGITS else []
        return []

    def is_final(self, state: str) -> bool:
        """Return True once the closing quote has been read."""

        return state == "done"

    def next_chars(self, state: str) -> Optional[Set[str]]:
        """Return the characters accepted in ``state``, None if unbounded."""

        if state == "start":
            return {'"'}
        if state in self.BODY:
            return None
        if state == "escape":
            return set(ESCAPES) | {"u"}
        if state in self.HEX_CHAIN:
            return set(HEXDIGITS)
        return set()


class BooleanAutomaton(ValueAutomaton):
    initial = ""
    WORDS = ("true", "false")

    def step(self, state: str, char: str) -> List[str]:
        candidate = state + char
        if any(word.startswith(candidate) for word in self.WORDS):
            return [candidate]
        return []

    def is_final(self, state: str) -> bool:
        return state in self.WORDS

    def next_chars(self, state: str) -> Optional[Set[str]]:
        return {
            word[len(state)]
            for word in self.WORDS
            if word.startswith(state) and len(word) > len(state)
        }


AUTOMATA: Dict[str, ValueAutomaton] = {
    "number": NumberAutomaton(),
    "integer": IntegerAutomaton(),
    "string": StringAutomaton(),
    "boolean": BooleanAutomaton(),
}

Part = Union[str, ValueAutomaton]


class Grammar:

    def __init__(self, functions: Sequence[FunctionDefinition]) -> None:
        if not functions:
            raise GrammarError(
                "no function definition to build a grammar from"
                )
        seen: Set[str] = set()
        self.templates: List[List[Part]] = []
        for function in functions:
            if function.name in seen:
                raise GrammarError(
                    "duplicated function name: %r" % function.name
                    )
            seen.add(function.name)
            self.templates.append(self._template(function))

    def _template(self, function: FunctionDefinition) -> List[Part]:
        parts: List[Part] = []
        buffer = '{"name": %s, "parameters": {' % json.dumps(function.name)
        for index, (key, param) in enumerate(function.parameters.items()):
            automaton = AUTOMATA.get(param.type)
            if automaton is None:
                raise GrammarError(
                    "%s: unsupported parameter type %r" % (
                        function.name, param.type
                        )
                )
            if index:
                buffer += ", "
            buffer += "%s: " % json.dumps(key)
            parts.append(buffer)
            parts.append(automaton)
            buffer = ""
        parts.append(buffer + "}}")
        return parts

    def start(self) -> "GrammarState":
        cursors = tuple(
            self.at(index, 0) for index in range(len(self.templates))
            )
        return GrammarState(self, cursors)

    def at(self, template: int, part: int) -> Cursor:
        parts = self.templates[template]
        if part >= len(parts):
            return (template, len(parts), 0)
        chunk = parts[part]
        if isinstance(chunk, str):
            return (template, part, 0)
        return (template, part, chunk.initial)

    def is_done(self, cursor: Cursor) -> bool:
        return cursor[1] >= len(self.templates[cursor[0]])

    def step(self, cursor: Cursor, char: str) -> List[Cursor]:
        template, part, position = cursor
        parts = self.templates[template]
        if part >= len(parts):
            return []
        chunk = parts[part]
        if isinstance(chunk, str):
            offset = int(position)
            if offset < len(chunk) and chunk[offset] == char:
                if offset + 1 == len(chunk):
                    return [self.at(template, part + 1)]
                return [(template, part, offset + 1)]
            return []
        state = str(position)
        reachable: List[Cursor] = [
            (template, part, nxt) for nxt in chunk.step(state, char)
        ]
        if chunk.is_final(state):
            reachable.extend(self.step(self.at(template, part + 1), char))
        return reachable

    def chars(self, cursor: Cursor) -> Optional[Set[str]]:
        template, part, position = cursor
        parts = self.templates[template]
        if part >= len(parts):
            return set()
        chunk = parts[part]
        if isinstance(chunk, str):
            return {chunk[int(position)]}
        state = str(position)
        allowed = chunk.next_chars(state)
        if not chunk.is_final(state):
            return allowed
        following = self.chars(self.at(template, part + 1))
        if allowed is None or following is None:
            return None
        return allowed | following


class GrammarState:

    def __init__(self, grammar: Grammar, cursors: Tuple[Cursor, ...]) -> None:
        self.grammar = grammar
        self.cursors = cursors

    def in_string(self) -> bool:
        """Return True if a cursor sits inside the body of a string value."""

        for template, part, position in self.cursors:
            parts = self.grammar.templates[template]
            if part >= len(parts):
                continue
            chunk = parts[part]
            if isinstance(chunk, StringAutomaton) and position in chunk.BODY:
                return True
        return False

    def is_complete(self) -> bool:
        return any(self.grammar.is_done(cursor) for cursor in self.cursors)

    def accepts(self, piece: str) -> bool:
        return bool(self._consume(piece))

    def advance(self, text: str) -> "GrammarState":
        cursors = self._consume(text)
        if not cursors:
            raise GrammarError("the grammar rejects %r" % text)
        return GrammarState(self.grammar, cursors)

    def forced_text(self) -> str:
        pieces: List[str] = []
        cursors = self.cursors
        while not any(self.grammar.is_done(cursor) for cursor in cursors):
            allowed = self._possible(cursors)
            if allowed is None or len(allowed) != 1:
                break
            char = next(iter(allowed))
            pieces.append(char)
            cursors = self._advance(cursors, char)
        return "".join(pieces)

    def _possible(self, cursors: Tuple[Cursor, ...]) -> Optional[Set[str]]:
        allowed: Set[str] = set()
        for cursor in cursors:
            chars = self.grammar.chars(cursor)
            if chars is None:
                return None
            allowed |= chars
            if len(allowed) > 1:
                return allowed
        return allowed

    def _advance(
            self, cursors: Tuple[Cursor, ...], char: str
            ) -> Tuple[Cursor, ...]:
        reached: Dict[Cursor, None] = {}
        for cursor in cursors:
            for nxt in self.grammar.step(cursor, char):
                reached[nxt] = None
        return tuple(reached)

    def _consume(self, text: str) -> Tuple[Cursor, ...]:
        cursors = self.cursors
        for char in text:
            cursors = self._advance(cursors, char)
            if not cursors:
                return ()
        return cursors
