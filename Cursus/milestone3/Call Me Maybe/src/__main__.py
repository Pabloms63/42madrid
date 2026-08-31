import argparse
import sys
from pathlib import Path
from typing import List, Sequence

from .decoder import DecodeError, Decoder
from .grammar import Grammar, GrammarError
from .llm_engine import DEFAULT_MODEL, EngineError, LLMEngine
from .loader import LoaderError, load_functions, load_prompts, write_results
from .models import FunctionCall, FunctionDefinition
from .parser import ParserError, parse_call
from .prompt import build_prompt


def parse_args() -> argparse.Namespace:
    """Read the command line arguments."""
    parser = argparse.ArgumentParser(prog="src")
    parser.add_argument(
        "--functions_definition",
        type=Path,
        default=Path("data/input/functions_definition.json"),
        help="JSON file describing the callable functions",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/input/function_calling_tests.json"),
        help="JSON file with the natural language prompts",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/output/function_calling_results.json"),
        help="where to write the generated calls",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="model to load through llm_sdk",
    )
    return parser.parse_args()


def run(
    decoder: Decoder,
    functions: Sequence[FunctionDefinition],
    requests: Sequence[str],
) -> List[FunctionCall]:
    """Decode every request, reporting the ones that fail without stopping."""
    calls: List[FunctionCall] = []
    for index, request in enumerate(requests, start=1):
        try:
            text = decoder.decode(build_prompt(functions, request))
            calls.append(parse_call(request, text, functions))
        except (DecodeError, GrammarError, ParserError, EngineError) as err:
            print("prompt %d skipped (%s)" % (index, err), file=sys.stderr)
    return calls


def main() -> int:
    """Run the whole pipeline and return the process exit code."""
    args = parse_args()
    try:
        functions = load_functions(args.functions_definition)
        prompts = load_prompts(args.input)
        engine = LLMEngine(args.model)
        decoder = Decoder(engine, engine.vocabulary(), Grammar(functions))
        calls = run(decoder, functions, [item.prompt for item in prompts])
        write_results(args.output, calls)
    except (LoaderError, EngineError, GrammarError, DecodeError) as err:
        print("error: %s" % err, file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("interrupted", file=sys.stderr)
        return 130

    print("%d/%d calls written to %s" % (len(calls), len(prompts), args.output))
    return 0 if len(calls) == len(prompts) else 1


if __name__ == "__main__":
    sys.exit(main())
