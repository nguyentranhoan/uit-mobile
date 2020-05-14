from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateUserFacebook(BaseModel):
    facebook_account: Optional[str]


class CreateUserEmail(BaseModel):
    email: EmailStr


class CreateUserNormal(BaseModel):
    normal_account: Optional[str]
    password: Optional[str]
    email: Optional[EmailStr]


class UpdateUserInfo(BaseModel):
    first_name: Optional[str]
    midle_name: Optional[str]
    last_name: Optional[str]
    password: Optional[str]
