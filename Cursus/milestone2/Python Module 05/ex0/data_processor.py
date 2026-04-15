from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Sequence


# Clase abstracta base
class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: List[Tuple[int, str]] = []
        self.next: int = 0

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

    def ingest(
        self,
        data: str | int | float | Sequence[str | int | float]
    ) -> None:
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

    def ingest(self, data: str | List[str]) -> None:
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
        return (
            isinstance(data, dict)
            and all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items())
            )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(self._is_log(item) for item in data)
        return self._is_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper Log Data")

        items = data if isinstance(data, list) else [data]

        try:
            for item in items:
                level = item.get("log_level", "UNKNOWN")
                message = item.get("log_message", "No data available")
                log_formatted = f"{level}: {message}"
                self.data.append((self.next, log_formatted))
                self.next += 1
        except Exception as e:
            raise RuntimeError(f"Log ingestion error: {e}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    # Tests of numeric processor
    num_processor = NumericProcessor()
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {num_processor.validate(42)}")
    print(
        f"Trying to validate input 'Hello':"
        f" {num_processor.validate('Hola')}"
    )
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_processor.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")
    list_nums = [1, 2, 3, 4, 5]
    try:
        num_processor.ingest(list_nums)
    except Exception as e:
        print(f"Got exception: {e}")
    print(f"Processing data: {list_nums}")
    print("Extracting 3 values...")
    for i in range(3):
        key, value = num_processor.output()
        print(f"Numeric value: {key}: {value}")

    # Tests of text processor
    text_processor = TextProcessor()
    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {text_processor.validate(42)}")
    list_strings = ['Hello', 'Nexus', 'World']
    try:
        text_processor.ingest(list_strings)
    except Exception as e:
        print(f"Got exception: {e}")
    print(f"Processing data: {[list_strings]}")
    print("Extracting 1 value...")
    key, value = text_processor.output()
    print(f"Text value {key}: {value}")

    # Tests of log processor
    log_processor = LogProcessor()
    print("\nTesting Log Processor...")
    print(
        f"Trying to validate input 'Hello':"
        f" {log_processor.validate('Hello')}")
    list_logs = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to sever'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {list_logs}")
    try:
        log_processor.ingest(list_logs)
    except Exception as e:
        print(f"Get exception: {e}")
    print("Extracting 2 values...")
    for i in range(2):
        key, value = log_processor.output()
        print(f"Log entry {key}: {value}")
