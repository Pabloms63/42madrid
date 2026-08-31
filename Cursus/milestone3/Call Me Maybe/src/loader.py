from pathlib import Path
import json
from typing import List
from pydantic import ValidationError
from .models import FunctionDefinition, PromptRequest, FunctionCall


class LoaderError(Exception):
    """Fallo al leer o escribir un fichero del proyecto."""


def _read_json(path: Path) -> object:
    try:
        with path.open(encoding="utf-8-sig") as handle:
            return json.load(handle)
    except FileNotFoundError as err:
        raise LoaderError(f"The file doesn't exists: {path}") from err
    except json.JSONDecodeError as err:
        raise LoaderError(f"Invalid JSON in  {path}: {err}") from err
    except OSError as err:
        raise LoaderError(f"Couldn't be read {path}: {err}") from err


def load_functions(path: Path) -> List[FunctionDefinition]:
    raw = _read_json(path)
    if not isinstance(raw, list):
        raise LoaderError(f"Expected a JSON array in {path}")
    try:
        return [FunctionDefinition.model_validate(item) for item in raw]
    except (ValidationError, TypeError) as err:
        raise LoaderError(f"Malformed definitions in {path}: {err}") from err


def load_prompts(path: Path) -> List[PromptRequest]:
    raw = _read_json(path)
    if not isinstance(raw, list):
        raise LoaderError(f"Expected a JSON array in {path}")
    try:
        return [PromptRequest.model_validate(item) for item in raw]
    except (ValidationError, TypeError) as err:
        raise LoaderError(f"Malformed prompts in {path}: {err}") from err


def write_results(path: Path, results: List[FunctionCall]) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = [r.model_dump() for r in results]
        with path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False)
    except OSError as err:
        raise LoaderError(f"Couldn't be written {path}: {err}") from err
