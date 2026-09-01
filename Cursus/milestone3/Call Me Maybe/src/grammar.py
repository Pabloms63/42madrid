"""Schema-aware grammar used to constrain the decoder.

Every function definition is turned into a template: an alternating sequence
of literal chunks and typed slots.  A ``GrammarState`` keeps one cursor per
template, so the set of live cursors *is* the set of calls still reachable
from the text generated so far.
"""

import json
from typing import Dict, List, Optional, Sequence, Set, Tuple, Union

from .models import FunctionDefinition

DIGITS = frozenset("0123456789")
HEXDIGITS = frozenset("0123456789abcdefABCDEF")
ESCAPES = frozenset('"\\/bfnrt')

# A cursor is (template index, part index, position inside that part).  The
# position is an offset for a literal and an automaton state for a slot.
Cursor = Tuple[int, int, Union[int, str]]


class GrammarError(Exception):
    """Raised when a grammar cannot be built or no longer accepts the text."""


class ValueAutomaton:
    """State machine recognising the JSON encoding of one parameter type."""

    initial: str = ""

    def step(self, state: str, char: str) -> List[str]:
        """Return the states reachable from ``state`` by reading ``char``."""
        raise NotImplementedError

    def is_final(self, state: str) -> bool:
        """Return True if ``state`` is a complete value."""
        raise NotImplementedError

    def next_chars(self, state: str) -> Optional[Set[str]]:
        """Return the characters accepted in ``state``, None if unbounded."""
        raise NotImplementedError


class NumberAutomaton(ValueAutomaton):
    """Recognise a JSON number, rejecting leading zeros and bare dots."""

    initial = "start"
    ALPHABET = "-+.eE0123456789"
    FINAL = frozenset({"zero", "integer", "fraction", "exponent_digit"})

    def step(self, state: str, char: str) -> List[str]:
        """Return the states reachable from ``state`` by reading ``char``."""
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
        """Return True if the digits read so far already form a number."""
        return state in self.FINAL

    def next_chars(self, state: str) -> Optional[Set[str]]:
        """Return the characters accepted in ``state``."""
        return {char for char in self.ALPHABET if self.step(state, char)}


class IntegerAutomaton(NumberAutomaton):
    """Recognise a JSON integer: no fraction and no exponent.

    A parameter typed ``integer`` reaches a function annotated ``int``, and
    ``4.0`` is not an ``int`` in Python.  Forbidding the decimal point in the
    grammar is what keeps that distinction, rather than rounding later and
    silently changing the value.
    """

    ALPHABET = "-0123456789"
    FINAL = frozenset({"zero", "integer"})

    def step(self, state: str, char: str) -> List[str]:
        """Return the states reachable from ``state`` by reading ``char``."""
        if char in ".eE":
            return []
        return super().step(state, char)


class StringAutomaton(ValueAutomaton):
    """Recognise a quoted JSON string, escapes included."""

    initial = "start"
    HEX_CHAIN = {"hex1": "hex2", "hex2": "hex3", "hex3": "hex4", "hex4": "body"}

    def step(self, state: str, char: str) -> List[str]:
        """Return the states reachable from ``state`` by reading ``char``."""
        if state == "start":
            return ["body"] if char == '"' else []
        if state == "body":
            if char == '"':
                return ["done"]
            if char == "\\":
                return ["escape"]
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
        if state == "body":
            return None
        if state == "escape":
            return set(ESCAPES) | {"u"}
        if state in self.HEX_CHAIN:
            return set(HEXDIGITS)
        return set()


class BooleanAutomaton(ValueAutomaton):
    """Recognise ``true`` or ``false``; the state is the prefix read so far."""

    initial = ""
    WORDS = ("true", "false")

    def step(self, state: str, char: str) -> List[str]:
        """Return the states reachable from ``state`` by reading ``char``."""
        candidate = state + char
        if any(word.startswith(candidate) for word in self.WORDS):
            return [candidate]
        return []

    def is_final(self, state: str) -> bool:
        """Return True if a whole keyword has been read."""
        return state in self.WORDS

    def next_chars(self, state: str) -> Optional[Set[str]]:
        """Return the characters accepted in ``state``."""
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
    """The set of JSON calls the decoder is allowed to produce."""

    def __init__(self, functions: Sequence[FunctionDefinition]) -> None:
        """Build one template per function definition.

        Args:
            functions: the available function definitions.

        Raises:
            GrammarError: if the definitions are empty, duplicated or use a
                parameter type the grammar cannot generate.
        """
        if not functions:
            raise GrammarError("no function definition to build a grammar from")
        seen: Set[str] = set()
        self.templates: List[List[Part]] = []
        for function in functions:
            if function.name in seen:
                raise GrammarError("duplicated function name: %r" % function.name)
            seen.add(function.name)
            self.templates.append(self._template(function))

    def _template(self, function: FunctionDefinition) -> List[Part]:
        """Turn one definition into literal chunks and typed slots."""
        parts: List[Part] = []
        buffer = '{"name": %s, "parameters": {' % json.dumps(function.name)
        for index, (key, param) in enumerate(function.parameters.items()):
            automaton = AUTOMATA.get(param.type)
            if automaton is None:
                raise GrammarError(
                    "%s: unsupported parameter type %r" % (function.name, param.type)
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
        """Return the state accepting every call, before any text is read."""
        cursors = tuple(self.at(index, 0) for index in range(len(self.templates)))
        return GrammarState(self, cursors)

    def at(self, template: int, part: int) -> Cursor:
        """Return the cursor entering part ``part`` of template ``template``."""
        parts = self.templates[template]
        if part >= len(parts):
            return (template, len(parts), 0)
        chunk = parts[part]
        if isinstance(chunk, str):
            return (template, part, 0)
        return (template, part, chunk.initial)

    def is_done(self, cursor: Cursor) -> bool:
        """Return True if ``cursor`` consumed its whole template."""
        return cursor[1] >= len(self.templates[cursor[0]])

    def step(self, cursor: Cursor, char: str) -> List[Cursor]:
        """Return the cursors reachable from ``cursor`` by reading ``char``.

        A slot that already holds a complete value may either keep growing or
        hand the character over to the next part; that is what lets a number
        end on the comma or the closing brace that follows it.
        """
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
        """Return the characters ``cursor`` accepts, None if unbounded."""
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
    """The set of calls still reachable from the text generated so far."""

    def __init__(self, grammar: Grammar, cursors: Tuple[Cursor, ...]) -> None:
        """Store the grammar and the live cursors."""
        self.grammar = grammar
        self.cursors = cursors

    def is_complete(self) -> bool:
        """Return True if one of the templates has been fully generated."""
        return any(self.grammar.is_done(cursor) for cursor in self.cursors)

    def accepts(self, piece: str) -> bool:
        """Return True if the whole token ``piece`` can be appended here."""
        return bool(self._consume(piece))

    def advance(self, text: str) -> "GrammarState":
        """Return the state reached after reading ``text``.

        Raises:
            GrammarError: if the text does not fit any of the templates.
        """
        cursors = self._consume(text)
        if not cursors:
            raise GrammarError("the grammar rejects %r" % text)
        return GrammarState(self.grammar, cursors)

    def forced_text(self) -> str:
        """Return the text that every reachable call shares from here.

        Whenever a single character is possible it carries no information, so
        it is emitted without asking the model: this collapses the punctuation,
        the parameter names and the common prefixes of the function names.
        """
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
        """Return the characters accepted by ``cursors``, None if unbounded."""
        allowed: Set[str] = set()
        for cursor in cursors:
            chars = self.grammar.chars(cursor)
            if chars is None:
                return None
            allowed |= chars
            if len(allowed) > 1:
                return allowed
        return allowed

    def _advance(self, cursors: Tuple[Cursor, ...], char: str) -> Tuple[Cursor, ...]:
        """Return the cursors reachable from ``cursors`` by reading ``char``."""
        reached: Dict[Cursor, None] = {}
        for cursor in cursors:
            for nxt in self.grammar.step(cursor, char):
                reached[nxt] = None
        return tuple(reached)

    def _consume(self, text: str) -> Tuple[Cursor, ...]:
        """Return the cursors left after reading ``text``, empty if rejected."""
        cursors = self.cursors
        for char in text:
            cursors = self._advance(cursors, char)
            if not cursors:
                return ()
        return cursors
