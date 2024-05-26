from pydantic import BaseModel, field_validator
from enum import Enum


class Model(str, Enum):
    gpt_4 = "gpt-4"
    gpt_3_5_turbo = "gpt-3.5-turbo"
    gpt_3_5_turbo_0125 = "gpt-3.5-turbo-0125"
    gpt_4_turbo = "gpt-4-turbo"
    gpt_4o = "gpt-4o"
    gpt_4_turbo_preview = "gpt-4-turbo-preview"


class GPTModel(BaseModel):
    model: Model

    @field_validator("model")
    def check_model(cls, value):
        if not isinstance(value, Model):
            raise ValueError(f"{value} is not a valid model.")
        return value

    def __str__(self):
        return self.model.value


class GPT_Request(BaseModel):
    model: GPTModel
    question: str
