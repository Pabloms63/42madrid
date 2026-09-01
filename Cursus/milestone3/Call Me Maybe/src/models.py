from pydantic import BaseModel, ConfigDict
from typing import Dict, Any, Literal


class FunctionParam(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: Literal[
        "number", "integer", "string", "boolean", "array", "object"
    ]


class FunctionDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    description: str
    parameters: Dict[str, FunctionParam]
    returns: FunctionParam


class PromptRequest(BaseModel):
    prompt: str


class FunctionCall(BaseModel):
    prompt: str
    name: str
    parameters: Dict[str, Any]
