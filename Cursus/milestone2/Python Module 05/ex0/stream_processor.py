from abc import ABC, abstractmethod
from typing import Any


# Clase abstracta base
class DataProcessor(ABC):
    def __init__(self, debug: bool = True):
        self.debug = debug

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


# Procesador de números
class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.debug:
            print("Initializing Numeric Processor...")
            print(f"Processing data: {data}")
        if not self.validate(data):
            raise ValueError("Invalid numeric data")
        if self.debug:
            print("Validation: Numeric data verified")
        length = len(data)
        total = sum(data)
        avg = total / length
        result = (
            f"Processed {length} numeric values, "
            f"sum={total}, avg={avg}"
            )
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
            )


# Procesador de texto
class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.debug:
            print("\nInitializing Text Processor...")
            print(f"Processing data: {data}")
        if not self.validate(data):
            raise ValueError("Invalid text data")
        if self.debug:
            print("Validation: Text data verified")
        len_string = len(data)
        total_words = len(data.split())
        result = (
            f"Processed text: {len_string} characters, {total_words} words"
        )
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


# Procesador de logs
class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.debug:
            print("\nInitializing Log Processor...")
            print(f'Processing data: "{data}"')
        if not self.validate(data):
            raise ValueError("Invalid log data")
        if self.debug:
            print("Validation: Log entry verified")
        if "ERROR" in data:
            level = "ALERT"
        else:
            level = "INFO"
        error = " ".join(data.split()[1:])
        result = f"[{level}] level detected: {error}"
        return self.format_output(result)

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
