from typing import List

from pydantic import BaseModel


class Choice(BaseModel):
    question_id: int
    type: str


class Result(BaseModel):
    choices: List[Choice]

