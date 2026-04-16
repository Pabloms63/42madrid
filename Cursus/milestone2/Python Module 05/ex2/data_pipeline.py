from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Protocol, Sequence


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream:
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processors.append(proc)
            # print(f"{type(proc).__name__} Processor registered")
        else:
            print("Error: Couldn't register data processor")

    def process_stream(self, stream: List[Any]) -> None:
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
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for p in self.processors:
            print(f"{type(p).__name__}: ", end="")
            print(f"total {p.next} items processed, ", end="")
            print(f"remaining {len(p.data)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for p in self.processors:
            to_export = []
            for _ in range((nb)):
                try:
                    to_export.append(p.output())
                except IndexError:
                    break
            if to_export:
                plugin.process_output(to_export)


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output")
        values = [v for r, v in data]
        print(", ".join(values))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output")
        items = []
        for rank, value in data:
            clean_value = value.replace("\n", " ")
            items.append(f'"item_{rank}": "{clean_value}"')
        print("{" + ", ".join(items) + "}")


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
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")

    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")

    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(num)
    stream.register_processor(text)
    stream.register_processor(log)

    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is' 'connected'}],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream {data}")

    stream.process_stream(data)
    stream.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVPlugin())
    stream.print_processors_stats()
    print("")
    DATA_POOL_2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
         ], [32, 42, 64, 84, 128, 168], 'World hello'
        ]

    print(f"Send another batch of data: {DATA_POOL_2}")
    stream.process_stream(DATA_POOL_2)
    stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONPlugin())
    print("")
    stream.print_processors_stats()
