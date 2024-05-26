from pydantic import BaseModel
from enum import Enum

# fastapi要求要pydantic


class Level(str, Enum):
    error = "error"
    warn = "warn"
    success = "success"


class NotifyRequest(BaseModel):
    level: Level
    message: str
