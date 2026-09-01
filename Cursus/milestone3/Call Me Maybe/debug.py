"""Inspect what the model wants to say, with and without the grammar."""

import json
from pathlib import Path

from src.grammar import Grammar
from src.llm_engine import LLMEngine
from src.loader import load_functions
from src.prompt import build_prompt

REQUEST = "Greet shrek"
TOP = 15


def main() -> None:
    functions = load_functions(Path("data/input/functions_definition.json"))
    engine = LLMEngine()
    vocab = engine.vocabulary()
    grammar = Grammar(functions)
    prompt = build_prompt(functions, REQUEST)

    print("=== prompt (%d chars) ===" % len(prompt))
    print(prompt)
    print("=== encoded to %d tokens ===" % len(engine.encode(prompt)))

    for generated in ['{"name": "fn', '{"name": "fn_g']:
        text = prompt + generated
        scores = engine.logits(engine.encode(text))
        order = sorted(range(len(scores)), key=lambda i: -scores[i])[:TOP]
        print("\n--- after %r ---" % generated)
        print("unconstrained top %d:" % TOP)
        for token_id in order:
            print("   %-10r %.2f" % (vocab.text(token_id), scores[token_id]))

        state = grammar.start()
        if generated:
            state = state.advance(generated)
        allowed = []
        for token_id in sorted(range(len(scores)), key=lambda i: -scores[i]):
            piece = vocab.text(token_id)
            if piece and state.accepts(piece):
                allowed.append((piece, scores[token_id]))
            if len(allowed) >= 10:
                break
        print("grammar allows, best first:")
        for piece, score in allowed:
            print("   %-10r %.2f" % (piece, score))

    print("\n=== full decode ===")
    from src.decoder import Decoder
    print(json.dumps(Decoder(engine, vocab, grammar).decode(prompt)))


if __name__ == "__main__":
    main()
