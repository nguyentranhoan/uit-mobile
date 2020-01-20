from pydantic import BaseModel


class Feedback(BaseModel):
    feedback: str


class IsLiked(BaseModel):
    is_liked: bool = True
