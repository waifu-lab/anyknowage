from enum import Enum

from pydantic import BaseModel

# fastapi要求要pydantic


class Level(str, Enum):
    error = "error"
    warn = "warn"
    success = "success"


class NotifyRequest(BaseModel):
    level: Level
    message: str


class LoggerRequest(BaseModel):
    message: str
