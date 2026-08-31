import re
from typing import FrozenSet, List, Optional, Sequence, Set, Tuple

from .models import FunctionDefinition

# A number still being written ("-", "1.", "1.5e-") and one allowed to stop.
_PARTIAL = re.compile(r"-?((0|[1-9][0-9]*)(\.[0-9]*)?([eE][+-]?[0-9]*)?)?")
_COMPLETE = re.compile(r"-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?")

_ESCAPABLE = set('"\\/bfnrt')
MAX_STRING_LENGTH = 512


class GrammarError(Exception):
    """Raised when the generated text violates the grammar."""


class _Segment:
    """One piece of a template: fixed text or a typed hole."""

    def extends(self, buffer: str, char: str) -> bool:
        """Return True if ``buffer + char`` is still a valid prefix."""
        raise NotImplementedError

    def is_final(self, buffer: str) -> bool:
        """Return True if ``buffer`` is a complete value for this segment."""
        raise NotImplementedError


class _Literal(_Segment):
    """Fixed text, reproduced verbatim."""

    def __init__(self, text: str) -> None:
        self.text = text

    def extends(self, buffer: str, char: str) -> bool:
        return len(buffer) < len(self.text) and self.text[len(buffer)] == char

    def is_final(self, buffer: str) -> bool:
        return buffer == self.text


class _Name(_Literal):
    """The function name.

    Fixed text like any literal, but the decoder must not write it for the
    model: forcing it character by character would land the model mid token,
    where its predictions are unreliable.
    """


class _Enum(_Segment):
    """A choice between fixed spellings, used for booleans."""

    def __init__(self, options: Sequence[str]) -> None:
        self.options = tuple(options)

    def extends(self, buffer: str, char: str) -> bool:
        return any(opt.startswith(buffer + char) for opt in self.options)

    def is_final(self, buffer: str) -> bool:
        return buffer in self.options


class _Number(_Segment):
    """A JSON number: no leading zero, no leading dot, optional exponent."""

    def extends(self, buffer: str, char: str) -> bool:
        return _PARTIAL.fullmatch(buffer + char) is not None

    def is_final(self, buffer: str) -> bool:
        return _COMPLETE.fullmatch(buffer) is not None


class _String(_Segment):
    r"""The inside of a JSON string; the quotes around it are literals.

    Only the short escapes are allowed (``\"``, ``\\``, ``\n``...), which is
    enough to carry regexes and quoted text while keeping the rule to one
    line: a backslash must be followed by an escapable character.
    """

    def extends(self, buffer: str, char: str) -> bool:
        if len(buffer) >= MAX_STRING_LENGTH:
            return False
        if self._escaping(buffer):
            return char in _ESCAPABLE
        return char == "\\" or (char >= " " and char != '"')

    def is_final(self, buffer: str) -> bool:
        return not self._escaping(buffer)

    @staticmethod
    def _escaping(buffer: str) -> bool:
        """Return True if the buffer ends on an unpaired backslash."""
        return (len(buffer) - len(buffer.rstrip("\\"))) % 2 == 1


# (plan index, segment index, text consumed so far in that segment)
_State = Tuple[int, int, str]


def _build_plan(function: FunctionDefinition) -> List[_Segment]:
    """Compile one function definition into an ordered list of segments."""
    plan: List[_Segment] = [_Literal('{"name": "'), _Name(function.name)]
    literal = '", "parameters": {'
    for key, param in function.parameters.items():
        literal += '"%s": ' % key
        if param.type == "string":
            plan += [_Literal(literal + '"'), _String()]
            literal = '", '
        elif param.type == "number":
            plan += [_Literal(literal), _Number()]
            literal = ", "
        else:
            plan += [_Literal(literal), _Enum(("true", "false"))]
            literal = ", "
    plan.append(_Literal(literal.rstrip(", ") + "}}"))
    return plan


class Grammar:
    """The set of templates the model is allowed to produce."""

    def __init__(self, functions: Sequence[FunctionDefinition]) -> None:
        if not functions:
            raise GrammarError("no function definition to build a grammar from")
        self.plans = [_build_plan(function) for function in functions]

    def start(self) -> "GrammarState":
        """Return the state in which nothing has been generated yet."""
        seeds = {(index, 0, "") for index in range(len(self.plans))}
        return GrammarState(self, frozenset(self._close(seeds)))

    def _close(self, states: Set[_State]) -> Set[_State]:
        """Add the states reached by declaring the current segment done."""
        closed: Set[_State] = set()
        pending = list(states)
        while pending:
            state = pending.pop()
            if state in closed:
                continue
            closed.add(state)
            plan, index, buffer = self.plans[state[0]], state[1], state[2]
            if index < len(plan) and plan[index].is_final(buffer):
                pending.append((state[0], index + 1, ""))
        return closed

    def step(self, states: FrozenSet[_State], char: str) -> FrozenSet[_State]:
        """Consume one character and return the states that survive it."""
        moved: Set[_State] = set()
        for plan_index, index, buffer in states:
            plan = self.plans[plan_index]
            if index < len(plan) and plan[index].extends(buffer, char):
                moved.add((plan_index, index, buffer + char))
        return frozenset(self._close(moved))


class GrammarState:
    """An immutable position inside the grammar.

    Immutable on purpose: the decoder tests many candidate tokens against the
    same position before committing to one of them.
    """

    def __init__(self, grammar: Grammar, states: FrozenSet[_State]) -> None:
        self.grammar = grammar
        self.states = states

    def accepts(self, text: str) -> bool:
        """Return True if ``text`` can be appended to the generated output."""
        states = self.states
        for char in text:
            states = self.grammar.step(states, char)
            if not states:
                return False
        return True

    def advance(self, text: str) -> "GrammarState":
        """Return the state reached after appending ``text``."""
        states = self.states
        for char in text:
            states = self.grammar.step(states, char)
            if not states:
                raise GrammarError("text rejected by the grammar: %r" % text)
        return GrammarState(self.grammar, states)

    def is_complete(self) -> bool:
        """Return True if the output is a finished, schema-valid call."""
        return any(
            index >= len(self.grammar.plans[plan_index])
            for plan_index, index, _ in self.states
        )

    def forced_text(self) -> str:
        """Return the text that is unavoidable from here, possibly empty.

        When a single character is legal the model has no choice to make, so
        the decoder emits it without asking the LLM for logits.  This is what
        makes the punctuation of the JSON skeleton free.
        """
        chunks: List[str] = []
        state = self
        while not state.is_complete():
            char = state._only_char()
            if char is None:
                break
            chunks.append(char)
            state = state.advance(char)
        return "".join(chunks)

    def _only_char(self) -> Optional[str]:
        """Return the single legal next character, or None if there are many."""
        found: Optional[str] = None
        for plan_index, index, buffer in self.states:
            plan = self.grammar.plans[plan_index]
            if index >= len(plan):
                return None
            segment = plan[index]
            if not isinstance(segment, _Literal) or isinstance(segment, _Name):
                return None
            if len(buffer) == len(segment.text):
                continue  # already closed, its successor is in the set
            char = segment.text[len(buffer)]
            if found is not None and found != char:
                return None
            found = char
        return found
