from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    hashed_password: str

    class Config:
        from_attributes = True
