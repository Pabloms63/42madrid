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
    """Interface every JSON value recogniser implements."""

    initial: str = ""

    def step(self, state: str, char: str) -> List[str]:
        """Return the states reachable from ``state`` by reading ``char``.

        An empty list means the character is rejected."""

        raise NotImplementedError

    def is_final(self, state: str) -> bool:
        """Return True if the value could legally end in ``state``."""

        raise NotImplementedError

    def next_chars(self, state: str) -> Optional[Set[str]]:
        """Return the characters accepted in ``state``, None if unbounded."""

        raise NotImplementedError


class NumberAutomaton(ValueAutomaton):
    """Recognise a JSON number: sign, digits, fraction and exponent."""

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
    """Recognise a JSON number with no fraction or exponent."""

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
    """Recognise ``true`` or ``false`` one character at a time."""

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
    """Hold one template per function and walk them in parallel.

    A template alternates literal text, which is known in advance, with
    automata for the values, which are not."""

    def __init__(self, functions: Sequence[FunctionDefinition]) -> None:
        """Build a template for every function.

        Args:
            functions: the definitions to accept.

        Raises:
            GrammarError: if the list is empty or a name is duplicated."""

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
        """Turn one definition into alternating text and automata.

        Punctuation and key names are accumulated in a buffer and flushed
        as a single part whenever a value automaton has to be inserted.

        Raises:
            GrammarError: if a parameter type has no automaton."""

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
        """Return a state sitting at the beginning of every template."""

        cursors = tuple(
            self.at(index, 0) for index in range(len(self.templates))
            )
        return GrammarState(self, cursors)

    def at(self, template: int, part: int) -> Cursor:
        """Return a cursor placed at the start of ``part``.

        Args:
            template: index of the template.
            part: index of the part within it, possibly past the end."""

        parts = self.templates[template]
        if part >= len(parts):
            return (template, len(parts), 0)
        chunk = parts[part]
        if isinstance(chunk, str):
            return (template, part, 0)
        return (template, part, chunk.initial)

    def is_done(self, cursor: Cursor) -> bool:
        """Return True if the cursor has run past the last part."""

        return cursor[1] >= len(self.templates[cursor[0]])

    def step(self, cursor: Cursor, char: str) -> List[Cursor]:
        """Return the cursors reachable from ``cursor`` by reading ``char``."""

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
        """Return the characters accepted at ``cursor``, None if unbounded."""

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
    """A position in every template that is still alive.

    Templates are explored in parallel: the function name is only settled
    once the text rules the other candidates out."""

    def __init__(self, grammar: Grammar, cursors: Tuple[Cursor, ...]) -> None:
        """Store the grammar and the cursors still viable."""

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
        """Return True if any cursor has reached the end of its template."""

        return any(self.grammar.is_done(cursor) for cursor in self.cursors)

    def accepts(self, piece: str) -> bool:
        """Return True if ``piece`` can be appended without breaking out."""

        return bool(self._consume(piece))

    def advance(self, text: str) -> "GrammarState":
        """Return the state reached after reading ``text``.

        Raises:
            GrammarError: if no template survives the text."""

        cursors = self._consume(text)
        if not cursors:
            raise GrammarError("the grammar rejects %r" % text)
        return GrammarState(self.grammar, cursors)

    def forced_text(self) -> str:
        """Return the characters that are the only ones possible from here."""

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
        """Return the characters any cursor accepts, None if unbounded."""

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
        """Return the cursors reachable by reading ``char``, deduplicated."""

        reached: Dict[Cursor, None] = {}
        for cursor in cursors:
            for nxt in self.grammar.step(cursor, char):
                reached[nxt] = None
        return tuple(reached)

    def _consume(self, text: str) -> Tuple[Cursor, ...]:
        """Return the cursors left after reading `text`, empty if rejected."""

        cursors = self.cursors
        for char in text:
            cursors = self._advance(cursors, char)
            if not cursors:
                return ()
        return cursors
