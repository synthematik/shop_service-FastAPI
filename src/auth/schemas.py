from pydantic import BaseModel, EmailStr


class RegisterSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str
