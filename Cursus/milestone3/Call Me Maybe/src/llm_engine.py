import json
import os
from typing import Any, List

from .vocabulary import Vocabulary

DEFAULT_MODEL = "Qwen/Qwen3-0.6B"


class EngineError(Exception):
    """Raised when the model cannot be loaded or queried."""


def _flatten(value: Any) -> List[int]:
    """Turn a tensor, a nested sequence or a list of ids into a flat list."""

    if hasattr(value, "tolist"):
        value = value.tolist()
    if isinstance(value, int):
        return [value]
    if isinstance(value, (list, tuple)):
        flat: List[int] = []
        for item in value:
            flat.extend(_flatten(item))
        return flat
    raise EngineError("unexpected encoding result: %r" % type(value))


class LLMEngine:
    """Expose the SDK as the ``LanguageModel`` protocol used by the decoder."""

    def __init__(self, model_name: str = DEFAULT_MODEL) -> None:
        """Load the model through the SDK
        Args:
            model_name: the model to load;
            defaults to the one the subject requires."""

        os.environ.setdefault("OMP_NUM_THREADS", str(os.cpu_count() or 1))
        try:
            from llm_sdk import Small_LLM_Model
        except ImportError as err:
            raise EngineError(
                "llm_sdk is not importable, copy it next to the src folder"
            ) from err
        try:
            self.model = Small_LLM_Model(model_name)
        except Exception as err:
            raise EngineError(
                "could not load %s: %s" % (model_name, err)
                ) from err

    def encode(self, text: str) -> List[int]:
        """Return the token ids of ``text``."""
        try:
            return _flatten(self.model.encode(text))
        except EngineError:
            raise
        except Exception as err:
            raise EngineError("encoding failed: %s" % err) from err

    def logits(self, input_ids: List[int]) -> List[float]:
        """Return the score of every token that could follow ``input_ids``."""
        if not input_ids:
            raise EngineError("cannot ask for logits on an empty input")
        try:
            scores = self.model.get_logits_from_input_ids(input_ids)
        except Exception as err:
            raise EngineError(
                "the model failed to produce logits: %s" % err
                ) from err
        if hasattr(scores, "tolist"):
            scores = scores.tolist()
        while isinstance(
            scores, list
            ) and scores and isinstance(
                scores[0], list
                ):
            scores = scores[-1]
        if not isinstance(scores, list) or not scores:
            raise EngineError("the model returned no logits")
        return [float(score) for score in scores]

    def vocabulary(self) -> Vocabulary:
        """Build the model through the SDK.
        Returns:
            A Vocabulary holding the text every token id produces."""

        try:
            path = self.model.get_path_to_vocab_file()
            with open(path, encoding="utf-8") as handle:
                size = len(json.load(handle))
            return Vocabulary(path, size)
        except (OSError, ValueError) as err:
            raise EngineError(
                "could not read the vocabulary file: %s" % err
                ) from err
        except Exception as err:
            raise EngineError(
                "the SDK did not provide a vocabulary: %s" % err
                ) from err
