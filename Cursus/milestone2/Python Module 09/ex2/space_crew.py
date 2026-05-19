from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError(" Mission ID must start with 'M'")

        has_leader = any(
            m.rank in [Rank.commander, Rank.captain] for m in self.crew
        )
        if not has_leader:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced_count = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced_count < (len(self.crew) / 2):
                raise ValueError(
                    "Long missions (> 365 days)"
                    " need 50% experienced crew (5+ years)"
                )

        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")

        return self


def space_crew_validation() -> None:
    print("Space Mission Crew Validation")
    print("=" * 42)

    try:
        sarah = CrewMember(
            member_id="COMM_04", name="Sarah Connor", rank=Rank.commander,
            age=56, specialization="Mission Command", years_experience=34,
            is_active=True
        )
        john = CrewMember(
            member_id="LIET_02", name="John Smith", rank=Rank.lieutenant,
            age=47, specialization="Navigation", years_experience=26,
            is_active=True
        )
        alice = CrewMember(
            member_id="OFFC_14", name="Alice Johnson", rank=Rank.officer,
            age=41, specialization="Engineering", years_experience=15,
            is_active=True
        )

        mission_valid = SpaceMission(
            mission_id="M2024_MARS", mission_name="Mars Colony Establishment",
            destination="Mars", launch_date=datetime(2024, 10, 10),
            duration_days=900, crew=[sarah, john, alice],
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission_valid.mission_name}")
        print(f"ID: {mission_valid.mission_id}")
        print(f"Destination: {mission_valid.destination}")
        print(f"Duration: {mission_valid.duration_days}")
        print(f"Budget: ${mission_valid.budget_millions}M")
        print(f"Crew size: {len(mission_valid.crew)}")
        print("Crew members:")
        for member in mission_valid.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")

    except ValidationError as e:
        print("Expected validation error:")
        error = e.errors()[0]
        message = error['msg'].replace("Value error, ", "")
        print(message)

    print("\n" + "=" * 42)
    try:
        mission_valid = SpaceMission(
            mission_id="M2024_MARS", mission_name="Mars Colony Establishment",
            destination="Mars", launch_date=datetime(2024, 10, 10),
            duration_days=900, crew=[john, alice], budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission_valid.mission_name}")
        print(f"ID: {mission_valid.mission_id}")
        print(f"Destination: {mission_valid.destination}")
        print(f"Duration: {mission_valid.duration_days}")
        print(f"Budget: ${mission_valid.budget_millions}M")
        print(f"Crew size: {len(mission_valid.crew)}")
        print("Crew members:")
        for member in mission_valid.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")

    except ValidationError as e:
        print("Expected validation error:")
        error = e.errors()[0]
        message = error['msg'].replace("Value error, ", "")
        print(message)


if __name__ == "__main__":
    space_crew_validation()
