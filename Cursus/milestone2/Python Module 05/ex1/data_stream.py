from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union

class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.total_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]) -> List[Any]:
        if criteria is None:
            return data_batch
        
        return [element for element in data_batch if isinstance(element, str) and criteria in element]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return{
            "stream_id": self.stream_id,
            "stream_type": self.__class__.__name__,
            "total_processed": self.total_processed
        }


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
        print(f"Processing sensor batch: {data_batch}")

        try:
            temps = []

            for element in data_batch:
                if isinstance(element, str) and ":" in element:
                    key, value = element.split(":")
                    if key.strip() == "temp":
                        temps.append(float(value))

            if not temps:
                return "No valid temperature data"

            avg = sum(temps) / len(temps)
            self.total_processed += len(temps)

            return f"Sensor analysis: {len(temps)} readings processed, avg temp: {avg:.2f}ºC"
        except Exception as e:
            return f"Sensor processing error: {str(e)}"


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")
        print(f"Processing transaction batch: {data_batch}")
        try:
            net = 0
            count = 0

            for element in data_batch:
                if isinstance(element, str) and ":" in element:
                    action, value = element.split(":")
                    action = action.strip()
                    amount = int(value)

                    if action == "buy":
                        net += amount
                        count += 1
                    elif action == "sell":
                        net -= count
                        count += 1

            self.total_processed += count
            sign = "+" if net >= 0 else ""
            return f"Transaction analysis: {count} operations, net flow: {sign}{net} units"

        except Exception as e:
            return f"Transaction analysis: {str(e)}"


class EventStream(DataStream):
    pass


if __name__ == "__main__":
    sensor = SensorStream("SENSOR_001")
    data_sensor = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(sensor.process_batch(data_sensor))

    transaction = TransactionStream("TRANS_001")
    data_trans = ["buy:100", "sell:150", "buy:75"]
    print(transaction.process_batch(data_trans))
