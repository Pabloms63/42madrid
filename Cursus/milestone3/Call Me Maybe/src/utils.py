"""Utilities for byte-level BPE vocabulary handling."""

import json
from functools import lru_cache


@lru_cache(maxsize=1)
def bytes_to_unicode() -> dict[int, str]:
    bs = (
        list(range(ord("!"), ord("~") + 1))
        + list(range(ord("¡"), ord("¬") + 1))
        + list(range(ord("®"), ord("ÿ") + 1))
    )
    cs = bs[:]
    n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return {b: chr(c) for b, c in zip(bs, cs)}


class Vocabulary:
    """Maps token ids to their real text representation."""

    def __init__(self, vocab_path: str, vocab_size: int) -> None:
        with open(vocab_path, encoding="utf-8") as handle:
            raw: dict[str, int] = json.load(handle)

        unicode_to_byte = {c: b for b, c in bytes_to_unicode().items()}
        self._id_to_text: dict[int, str] = {}

        for token, token_id in raw.items():
            try:
                data = bytes(unicode_to_byte[ch] for ch in token)
                self._id_to_text[token_id] = data.decode("utf-8")
            except (KeyError, UnicodeDecodeError):
                continue  # token no representable como texto limpio

        self.size = vocab_size

    def text(self, token_id: int) -> str | None:
        """Return the token text, or None when the id has no usable mapping."""
        return self._id_to_text.get(token_id)

    def ids(self) -> list[int]:
        """All token ids that have a usable text mapping."""
        return list(self._id_to_text)
