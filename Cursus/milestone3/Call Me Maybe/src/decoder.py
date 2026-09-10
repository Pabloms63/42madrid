from typing import Dict, List, Protocol, Tuple

import numpy as np

from .grammar import Grammar, GrammarState
from .vocabulary import Vocabulary

# A call is a few dozen tokens; anything longer is a runaway generation.
MAX_TOKENS = 256


def healable(text: str) -> bool:
    """Return True if ``text`` sits inside a word rather than on a boundary."""

    return bool(text) and all(char.isalnum() or char == "_" for char in text)


class DecodeError(Exception):
    """Raised when no valid call can be generated for a prompt."""


class LanguageModel(Protocol):
    """The part of the LLM SDK the decoder relies on."""

    def encode(self, text: str) -> List[int]:
        """Turn text into the token ids the model consumes."""
        ...

    def logits(self, input_ids: List[int]) -> List[float]:
        """Return the scores of every token following ``input_ids``."""
        ...


class Decoder:
    """Generate schema-valid function calls with constrained decoding."""

    def __init__(
        self,
        model: LanguageModel,
        vocabulary: Vocabulary,
        grammar: Grammar,
        max_tokens: int = MAX_TOKENS,
        margin: float = 6.0,
    ) -> None:
        self.margin = margin
        self.model = model
        self.grammar = grammar
        self.max_tokens = max_tokens
        self.pieces: Dict[int, str] = {
            token_id: vocabulary.text(token_id) or ""
            for token_id in vocabulary.ids()
        }
        # Tokens that decode to nothing can never help, drop them once.
        self.token_ids = np.array(
            [key for key, text in self.pieces.items() if text], dtype=np.int64
        )
        if self.token_ids.size == 0:
            raise DecodeError("the vocabulary contains no usable token")
        self.highest_id = int(self.token_ids.max())
        self.forwards = 0

    def _fits(self, state: GrammarState, text: str, escaping: bool) -> str:
        """Return the text to keep for ``text``,
        empty if the grammar refuses."""

        if state.accepts(text):
            return text
        if not escaping:
            return ""
        if text.startswith(" ") and state.accepts(text[1:]):
            return text[1:]
        if '"' in text:
            escaped = text.replace('"', '\\"')
            if state.accepts(escaped):
                return escaped
        return ""

    def decode(self, prompt: str) -> str:
        """Return the JSON call generated for ``prompt``."""

        state = self.grammar.start()
        generated = ""
        steps = 0
        just_forced = False
        while not state.is_complete():
            forced = state.forced_text()
            if forced:
                generated += forced
                state = state.advance(forced)
                just_forced = True
                continue
            if steps >= self.max_tokens:
                raise DecodeError("token budget exhausted: %r" % generated)
            piece = self._next_piece(prompt, generated, state, just_forced)
            generated += piece
            state = state.advance(piece)
            just_forced = False
            steps += 1
        return generated

    def _split(
        self, prompt: str, generated: str, forced: bool
    ) -> Tuple[str, str]:
        """Split the text into the part to encode and the part to re-decide."""

        text = prompt + generated
        if not forced:
            return text, ""
        ids = self.model.encode(text)
        if not ids:
            return text, ""
        tail = self.pieces.get(int(ids[-1]), "")
        if not (tail and generated.endswith(tail) and healable(tail)):
            return text, ""
        return text[:len(text) - len(tail)], tail

    def _search(
        self, scores: np.ndarray, state: GrammarState, tail: str
    ) -> str:
        """Return the best token extending ``tail``
        that the grammar accepts."""

        candidates = self.token_ids[np.argsort(-scores[self.token_ids])]
        escaping = state.in_string()
        best = ""
        ceiling = 0.0
        for token_id in candidates:
            score = float(scores[token_id])
            if best and score < ceiling - self.margin:
                break
            piece = self.pieces[int(token_id)]
            # The token has to reproduce the healed characters and add to
            # them, otherwise it makes no progress.
            if not piece.startswith(tail) or len(piece) == len(tail):
                continue
            text = self._fits(state, piece[len(tail):], escaping)
            if not text:
                continue
            piece = tail + text
            if not best:
                best, ceiling = piece, score
            elif len(piece) > len(best) and piece.startswith(best):
                best = piece
        return best

    def _next_piece(
        self, prompt: str, generated: str, state: GrammarState,
        forced: bool = False,
    ) -> str:
        """Return the text to append at this position."""

        head, tail = self._split(prompt, generated, forced)

        self.forwards += 1
        scores = np.asarray(
            self.model.logits(self.model.encode(head)), dtype=np.float64
        )
        if scores.size <= self.highest_id:
            raise DecodeError("the model returned fewer logits than tokens")

        best = self._search(scores, state, tail)
        if not best and tail:
            # No token extends the healed characters.  Rather than fail, ask
            # again from the whole text: healing can only ever help, never
            # take a call away.
            self.forwards += 1
            scores = np.asarray(
                self.model.logits(self.model.encode(prompt + generated)),
                dtype=np.float64,
            )
            best, tail = self._search(scores, state, ""), ""
        if not best:
            raise DecodeError("no token of the vocabulary fits the grammar")
        return best[len(tail):]
