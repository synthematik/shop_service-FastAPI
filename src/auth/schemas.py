from pydantic import BaseModel, EmailStr


class AuthSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str
