"""Inspect what the model wants to say, with and without the grammar."""

import json
from pathlib import Path
from typing import List, Sequence

from src.decoder import Decoder
from src.grammar import Grammar
from src.llm_engine import LLMEngine
from src.loader import load_functions
from src.models import FunctionDefinition
from src.prompt import build_prompt

REQUEST = "Read the file config.yaml using utf-8"
TOP = 15


def prefixes(functions: Sequence[FunctionDefinition]) -> List[str]:
    """Return two partial calls, the second one further into a name."""

    name = functions[0].name
    return ['{"name": "%s' % name[:cut] for cut in (2, 4)]


def main() -> None:
    """Print the top tokens the model wants, before and after filtering."""

    functions = load_functions(Path("data/input/functions_definition.json"))
    engine = LLMEngine()
    vocab = engine.vocabulary()
    grammar = Grammar(functions)
    prompt = build_prompt(functions, REQUEST)

    print("=== prompt (%d chars) ===" % len(prompt))
    print(prompt)
    print("=== encoded to %d tokens ===" % len(engine.encode(prompt)))

    for generated in prefixes(functions):
        text = prompt + generated
        scores = engine.logits(engine.encode(text))
        order = sorted(range(len(scores)), key=lambda i: -scores[i])
        print("\n--- after %r ---" % generated)
        print("unconstrained top %d:" % TOP)
        for token_id in order[:TOP]:
            print("   %-10r %.2f" % (vocab.text(token_id), scores[token_id]))

        state = grammar.start().advance(generated)
        allowed = []
        for token_id in order:
            piece = vocab.text(token_id)
            if piece and state.accepts(piece):
                allowed.append((piece, scores[token_id]))
            if len(allowed) >= 10:
                break
        print("grammar allows, best first:")
        for piece, score in allowed:
            print("   %-10r %.2f" % (piece, score))

    print("\n=== full decode ===")
    print(json.dumps(Decoder(engine, vocab, grammar).decode(prompt)))


if __name__ == "__main__":
    main()
