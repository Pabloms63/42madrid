from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Sequence


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


class DataStream:
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processors.append(proc)
            # print(f"{type(proc).__name__} Processor registered")
        else:
            print("Error: Couldn't register data processor")

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            found = False
            for p in self.processors:
                if p.validate(item):
                    p.ingest(item)
                    found = True
                    break
            if not found:
                print(f"Data Stream Error - Can't process element: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        
        for p in self.processors:
            print(f"{type(p).__name__}: ", end="")
            print(f"total {p.next} items processed, ", end="")
            print(f"remaining {len(p.data)} on processor")
    

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
    print("=== Code Nexus - Data Stream ===\n")

    print("Iniatilize Data Stream...")
    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]

    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")

    num_processor = NumericProcessor()
    data_stream.register_processor(num_processor)

    print(f"Send first batch of data on stream: {data}")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)
    print("Send the same batch again")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_processor.output()
    for _ in range(2):
        text_processor.output()
    log_processor.output()
    data_stream.print_processors_stats()
