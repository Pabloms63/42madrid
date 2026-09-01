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
    """Validate ``text`` against ``functions`` and build the call.

    Args:
        prompt: the original request, copied into the result.
        text: the JSON produced by the decoder.
        functions: the available function definitions.

    Returns:
        The validated call.

    Raises:
        ParserError: if the text is not a call matching one of the functions.
    """
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as err:
        raise ParserError("the generated text is not valid JSON: %s" % err) from err
    if not isinstance(payload, dict):
        raise ParserError("expected a JSON object, got %s" % type(payload).__name__)

    name = payload.get("name")
    definitions: Dict[str, FunctionDefinition] = {fn.name: fn for fn in functions}
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
    """Return True if ``value`` has the JSON type ``expected``."""
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    return isinstance(value, str)


def _coerce(value: object, expected: str) -> object:
    """Return ``value`` as the Python type the definition asks for.

    JSON draws no line between ``2`` and ``2.0``, but the function receiving
    the call does: a parameter declared ``number`` stands for a ``float``, and
    reading one back as ``int`` is enough to make a strict callee reject it.
    The grammar has already ruled out anything that could lose information
    here, so the conversion is safe.
    """
    if expected == "number":
        return float(value)  # type: ignore[arg-type]
    if expected == "integer":
        return int(value)  # type: ignore[arg-type]
    return value
