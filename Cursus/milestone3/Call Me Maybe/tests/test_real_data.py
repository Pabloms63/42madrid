"""Check the grammar against whatever functions the input file declares.

Nothing here names a function or a parameter: the assertions have to hold
for any definition file, including the one used during the peer review.
"""

import json
from pathlib import Path
from typing import Any, Dict, Sequence

from src.grammar import Grammar
from src.loader import load_functions
from src.models import FunctionDefinition
from src.parser import parse_call

ROOT = Path(__file__).resolve().parent.parent
DEFINITIONS = ROOT / "data" / "input" / "functions_definition.json"

# The smallest legal value of every type the grammar knows about.
SAMPLES: Dict[str, Any] = {
    "number": 0,
    "integer": 0,
    "string": "",
    "boolean": True,
}


def minimal_call(function: FunctionDefinition) -> str:
    """Return the shortest valid JSON call to ``function``."""

    parameters = {
        name: SAMPLES[param.type]
        for name, param in function.parameters.items()
    }
    return json.dumps(
        {"name": function.name, "parameters": parameters},
        separators=(", ", ": "),
    )


def check(functions: Sequence[FunctionDefinition]) -> None:
    """Assert the grammar handles every declared function."""

    grammar = Grammar(functions)
    assert len(grammar.templates) == len(functions), "one template each"
    assert grammar.start().forced_text(), "the prefix must be forced"

    for function in functions:
        text = minimal_call(function)
        state = grammar.start().advance(text)
        assert state.is_complete(), "grammar refused %s" % text
        call = parse_call("p", text, functions)
        assert call.name == function.name
        assert set(call.parameters) == set(function.parameters)
        print("ok  ", text)


def main() -> None:
    """Run the checks over the real definition file."""

    functions = load_functions(DEFINITIONS)
    print("%d functions declared in %s" % (len(functions), DEFINITIONS.name))
    unsupported = {
        param.type
        for function in functions
        for param in function.parameters.values()
    } - set(SAMPLES)
    assert not unsupported, "unsupported parameter types: %s" % unsupported
    check(functions)
    print("real data ok")


if __name__ == "__main__":
    main()
