from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Union


# Clase abstracta base
class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.data: List[Tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise IndexError("No data available")
        return self.data.pop(0)


# Procesador de números
class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            if all(isinstance(_, (int, float)) for _ in data):
                return True
        return False
    
    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        try:
            for item in items:
                self.data.append((self.next, str(item)))
                self.next += 1
        except Exception as e:
            raise RuntimeError(f"Numeric data corruption (fatal crash): {e}")


# Procesador de texto
class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if all(isinstance(_, str) for _ in data):
                return True
        return False
    
    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        try:
            for item in items:
                self.data.append((self.next, item))
                self.next += 1
        except Exception as e:
            raise RuntimeError(f"Text ingestion error: {e}")


# Procesador de logs
class LogProcessor(DataProcessor):
    def _is_log(self, data: Any) -> bool:
        return {
            isinstance(data, dict) and all(isinstance(key, str) and isinstance(value, str)
            for key, value in data.items())
        }

    def validate(self, data):
        return isinstance(data, str) and len(data) > 0

    def format_output(self, result: str) -> str:
        return super().format_output(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    p1 = NumericProcessor()
    print(p1.process([1, 2, 3, 4, 5]))

    p2 = TextProcessor()
    print(p2.process("Hello Nexus World"))

    p3 = LogProcessor()
    print(p3.process("ERROR: Connection timeout"))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [
        NumericProcessor(False),
        TextProcessor(False),
        LogProcessor(False)
    ]
    data_samples = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready"
    ]

    for i, processor in enumerate(processors):
        try:
            result = processor.process(data_samples[i])
            clean = result.replace("Output: ", "")
            print(f"Result {i+1}: {clean}")
        except ValueError as e:
            print(f"Error: {e}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")
