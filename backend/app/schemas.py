from typing import Any
from pydantic import BaseModel, Field

class Submission(BaseModel):
    player: str = Field(default="player", min_length=1, max_length=40)
    flag: str = Field(min_length=1, max_length=200)

class ChallengeRequest(BaseModel):
    payload: dict[str, Any] = Field(default_factory=dict)
