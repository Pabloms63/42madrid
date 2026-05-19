from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    is_operational: bool = True
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    notes: Optional[str] = Field(None, max_length=200)


def station_validation() -> None:
    print("Space Station Data Validation")
    print("=" * 42)

    try:
        station_valid = SpaceStation(
            station_id="ISS01", name="International Space Station",
            is_operational=True, crew_size=6, power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 4, 25, 14, 30, 0),
            notes="All systems nominal"
        )

        print("Valid station created:")
        print(f"ID: {station_valid.station_id}")
        print(f"Name: {station_valid.name}")
        print(f"Crew: {station_valid.crew_size} people")
        print(f"Power: {station_valid.power_level}%")
        print(f"Oxygen: {station_valid.oxygen_level}%")
        if station_valid.is_operational:
            status_error = "Operational"
        else:
            status_error = "Down"
        print(f"Status: {status_error}\n")

    except ValidationError as e:
        error = e.errors()[0]
        attribute_name = error['loc'][0]
        error_message = error['msg']
        print("Expected validation error:")
        print(f"{attribute_name} -> {error_message}")

    print("=" * 42)
    try:
        station_invalid = SpaceStation(
            station_id="ISS01", name="International Space Station",
            is_operational=True, crew_size=21, power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 4, 25, 14, 30, 0),
            notes="All systems nominal"
        )

        print("Valid station created:")
        print(f"ID: {station_invalid.station_id}")
        print(f"Name: {station_invalid.name}")
        print(f"Crew: {station_invalid.crew_size} people")
        print(f"Power: {station_invalid.power_level}%")
        print(f"Oxygen: {station_invalid.oxygen_level}%")
        if station_invalid.is_operational:
            status_error = "Operational"
        else:
            status_error = "Down"
        print(f"Status: {status_error}\n")

    except ValidationError as e:
        error = e.errors()[0]
        attribute_name = error['loc'][0]
        error_message = error['msg']
        print("Expected validation error:")
        print(f"{attribute_name} -> {error_message}")


if __name__ == "__main__":
    station_validation()
