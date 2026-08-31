"""Build the text sent to the model before constrained decoding starts.

The prompt is not what makes the output valid JSON: the grammar does that.
Its only job is to give the model what it needs to make two decisions well,
which function fits the request and which values the arguments take.  So it
lists the callable functions, then the request, and stops right where the JSON
call begins.

Every token of the prompt is re-encoded on every forward pass, and there is
one forward pass per generated token, so the prompt is kept as short as it can
be without hurting accuracy.
"""

from typing import Sequence, Set

from .models import FunctionDefinition

# How many leading characters two names must share to be called ambiguous.
PREFIX = 4

SYSTEM = (
    "Call one of these functions to answer the request.\n"
    "Copy argument values from the request, keeping spelling and case.\n"
)

# Qwen3 reasons before answering unless the thinking block is already closed.
# Leaving it open would make the model write prose the grammar has to reject.
CHAT_TEMPLATE = (
    "<|im_start|>system\n{system}<|im_end|>\n"
    "<|im_start|>user\n{request}<|im_end|>\n"
    "<|im_start|>assistant\n<think>\n\n</think>\n"
)

PLAIN_TEMPLATE = "{system}\nRequest: {request}\nCall: "


def ambiguous(functions: Sequence[FunctionDefinition]) -> Set[str]:
    """Return the names another name could be confused with.

    The model picks a function by generating its name, so two names sharing
    their first characters are a fork it has to resolve early, on the little
    evidence the shared prefix gives it.  Those names keep their description;
    the rest are clear enough on their own.
    """
    names = [function.name for function in functions]
    return {
        name
        for name in names
        if any(other != name and other[:PREFIX] == name[:PREFIX]
               for other in names)
    }


def describe(function: FunctionDefinition, verbose: bool) -> str:
    """Render one function as a signature, with its description if needed."""
    arguments = ", ".join(
        "%s: %s" % (name, param.type)
        for name, param in function.parameters.items()
    )
    signature = "- %s(%s)" % (function.name, arguments)
    if verbose:
        return "%s: %s" % (signature, function.description)
    return signature


def catalogue(functions: Sequence[FunctionDefinition]) -> str:
    """Render every available function, one line each."""
    unclear = ambiguous(functions)
    return "\n".join(
        describe(function, function.name in unclear) for function in functions
    )


def build_prompt(
    functions: Sequence[FunctionDefinition],
    request: str,
    chat_template: bool = True,
) -> str:
    """Return the full prompt for ``request``.

    Args:
        functions: the callable functions, as loaded from the definition file.
        request: the natural language prompt to translate.
        chat_template: wrap the prompt in Qwen's chat markup.  Turn it off for
            a base model that was not instruction tuned.

    Returns:
        The text to encode and feed to the model.
    """
    system = "%s\nAvailable functions:\n%s" % (SYSTEM, catalogue(functions))
    template = CHAT_TEMPLATE if chat_template else PLAIN_TEMPLATE
    return template.format(system=system, request=request.strip())
