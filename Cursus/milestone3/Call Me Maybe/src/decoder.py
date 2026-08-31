from typing import Dict, List, Protocol

import numpy as np

from .grammar import Grammar, GrammarState
from .vocabulary import Vocabulary

# A call is a few dozen tokens; anything longer is a runaway generation.
MAX_TOKENS = 256


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

    def decode(self, prompt: str) -> str:
        """Return the JSON call generated for ``prompt``.

        The result is guaranteed to parse and to match the schema of one of
        the functions the grammar was built from.
        """
        state = self.grammar.start()
        generated = ""
        steps = 0
        while not state.is_complete():
            forced = state.forced_text()
            if forced:
                generated += forced
                state = state.advance(forced)
                continue
            if steps >= self.max_tokens:
                raise DecodeError("token budget exhausted: %r" % generated)
            piece = self._next_piece(prompt + generated, state)
            generated += piece
            state = state.advance(piece)
            steps += 1
        return generated

    def _next_piece(self, text: str, state: GrammarState) -> str:
        """Return the token to append at this position.

        Among the tokens the grammar accepts, the highest scoring one is the
        greedy answer.  When another token within ``margin`` of it merely
        extends it, that longer token is taken instead: it commits to the same
        text but covers more ground, which saves whole forward passes.
        """
        self.forwards += 1
        scores = np.asarray(
            self.model.logits(self.model.encode(text)), dtype=np.float64
        )
        if scores.size <= self.highest_id:
            raise DecodeError("the model returned fewer logits than tokens")
        candidates = self.token_ids[np.argsort(-scores[self.token_ids])]
        best = ""
        ceiling = 0.0
        for token_id in candidates:
            score = float(scores[token_id])
            if best and score < ceiling - self.margin:
                break
            piece = self.pieces[int(token_id)]
            if not state.accepts(piece):
                continue
            if not best:
                best, ceiling = piece, score
            elif len(piece) > len(best) and piece.startswith(best):
                best = piece
        if not best:
            raise DecodeError("no token of the vocabulary fits the grammar")
        return best
