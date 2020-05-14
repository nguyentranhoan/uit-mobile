from pydantic import BaseModel, EmailStr


class LoginUserFacebook(BaseModel):
    facebook_account: str


class LoginUserEmail(BaseModel):
    email: EmailStr


class LoginUserNormal(BaseModel):
    normal_account: str
    password: str

