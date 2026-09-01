"""Count how many forward passes each prompt costs, and how long they take."""

import time
from pathlib import Path

from src.decoder import Decoder
from src.grammar import Grammar
from src.llm_engine import LLMEngine
from src.loader import load_functions, load_prompts
from src.prompt import build_prompt


def main() -> None:
    functions = load_functions(Path("data/input/functions_definition.json"))
    prompts = load_prompts(Path("data/input/function_calling_tests.json"))
    engine = LLMEngine()
    decoder = Decoder(engine, engine.vocabulary(), Grammar(functions))

    total_forwards = 0
    total_time = 0.0
    for item in prompts:
        decoder.forwards = 0
        start = time.time()
        try:
            call = decoder.decode(build_prompt(functions, item.prompt))
        except Exception as err:
            call = "FAILED: %s" % err
        elapsed = time.time() - start
        total_forwards += decoder.forwards
        total_time += elapsed
        print("%3d fwd  %6.1fs  %s" % (decoder.forwards, elapsed, call))

    print("\ntotal: %d forwards, %.1fs" % (total_forwards, total_time))
    if total_forwards:
        print("%.2fs per forward" % (total_time / total_forwards))


if __name__ == "__main__":
    main()
