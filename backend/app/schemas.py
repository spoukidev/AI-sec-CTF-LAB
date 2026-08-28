from typing import Any
from pydantic import BaseModel, Field, field_validator

class Submission(BaseModel):
    player: str = Field(default="player", min_length=1, max_length=40)
    flag: str = Field(min_length=1, max_length=200)

    @field_validator("player")
    @classmethod
    def normalize_player(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("player must contain non-whitespace characters")
        return normalized

class ChallengeRequest(BaseModel):
    payload: dict[str, Any] = Field(default_factory=dict)
