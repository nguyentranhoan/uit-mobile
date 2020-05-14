from pydantic import BaseModel, EmailStr


class ResetPassword(BaseModel):
    email: EmailStr
    new_password: str
