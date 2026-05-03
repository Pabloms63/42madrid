from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_business_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def alien_validation() -> None:
    print("Alien Contact Log Validation")
    print("=" * 42)

    try:
        report_valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 5, 3, 12, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )

        print("Valid contact report:")
        print(f"ID: {report_valid.contact_id}")
        print(f"Type: {report_valid.contact_type.value}")
        print(f"Location: {report_valid.location}")
        print(f"Signal: {report_valid.signal_strength}/10")
        print(f"Duration: {report_valid.duration_minutes} minutes")
        print(f"Witnesses: {report_valid.witness_count}")
        print(f"Message: '{report_valid.message_received}'\n")

    except ValidationError as e:
        error = e.errors()[0]
        message = error['msg'].replace("Value error, ", "")
        print(message)

    print("=" * 42)
    try:
        report_invalid = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 5, 3, 12, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )

        print("Valid contact report:")
        print(f"ID: {report_invalid.contact_id}")
        print(f"Type: {report_invalid.contact_type.value}")
        print(f"Location: {report_invalid.location}")
        print(f"Signal: {report_invalid.signal_strength}/10")
        print(f"Duration: {report_invalid.duration_minutes} minutes")
        print(f"Witnesses: {report_invalid.witness_count}")
        print(f"Message: '{report_invalid.message_received}'\n")

    except ValidationError as e:
        error = e.errors()[0]
        message = error['msg'].replace("Value error, ", "")
        print(message)


if __name__ == "__main__":
    alien_validation()
