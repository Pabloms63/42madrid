from pydantic import BaseModel
from typing import Dict, Any, Literal


class FunctionParam(BaseModel):
    type: Literal["number", "string", "boolean"]

class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: Dict[str, FunctionParam]
    returns: FunctionParam

class PromptRequest(BaseModel):
    prompt: str

class FunctionCallResult(BaseModel):
    prompt: str
    fn_name: str
    args: Dict[str, Any]
