import json
from typing import Dict, Sequence

from .models import FunctionCall, FunctionDefinition


class ParserError(Exception):
    """Raised when the generated text does not match any definition."""


def parse_call(
    prompt: str,
    text: str,
    functions: Sequence[FunctionDefinition],
) -> FunctionCall:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as err:
        raise ParserError(
            "the generated text is not valid JSON: %s" % err
            ) from err
    if not isinstance(payload, dict):
        raise ParserError(
            "expected a JSON object, got %s" % type(payload).__name__
            )

    name = payload.get("name")
    definitions: Dict[str, FunctionDefinition] = {
        fn.name: fn for fn in functions
        }
    if not isinstance(name, str) or name not in definitions:
        raise ParserError("unknown function name: %r" % (name,))

    parameters = payload.get("parameters")
    if not isinstance(parameters, dict):
        raise ParserError("the parameters of %s are not an object" % name)

    expected = definitions[name].parameters
    if set(parameters) != set(expected):
        raise ParserError(
            "%s expects %s, got %s"
            % (name, sorted(expected), sorted(parameters))
        )
    values = dict(parameters)
    for key, param in expected.items():
        if not _matches(values[key], param.type):
            raise ParserError(
                "argument %r of %s should be a %s" % (key, name, param.type)
            )
        values[key] = _coerce(values[key], param.type)
    return FunctionCall(prompt=prompt, name=name, parameters=values)


def _matches(value: object, expected: str) -> bool:
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    return isinstance(value, str)


def _coerce(value: object, expected: str) -> object:
    if expected == "number" and isinstance(value, int) \
            and not isinstance(value, bool):
        return float(value)
    return value
