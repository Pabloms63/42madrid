from pydantic import BaseModel, ConfigDict
from typing import Dict, Any, Literal


class FunctionParam(BaseModel):
    """The declared type of a single argument of return value."""

    model_config = ConfigDict(extra="forbid")
    type: Literal[
        "number", "integer", "string", "boolean", "array", "object"
    ]


class FunctionDefinition(BaseModel):
    """One callable function, as described by the input file."""

    model_config = ConfigDict(extra="forbid")
    name: str
    description: str
    parameters: Dict[str, FunctionParam]
    returns: FunctionParam


class PromptRequest(BaseModel):
    """A single natural language request read from the input file."""

    prompt: str


class FunctionCall(BaseModel):
    """A resolved call, ready to be written to the output file."""

    prompt: str
    name: str
    parameters: Dict[str, Any]
