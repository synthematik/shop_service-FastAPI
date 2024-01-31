from fastapi import APIRouter
from src.auth.schemas import AuthSchema
from src.users.service import UserService
from src.auth.exception import *
from src.auth.auth import get_password_hash


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register/")
async def register_user(user_data: AuthSchema):
    existing_user = await UserService.find_user_by_email(user_data.email)
    if existing_user:
        raise UserAlreadyExistsException()
    hashed_password = get_password_hash(user_data.password)
    await UserService.add(
        name=user_data.name,
        last_name=user_data.last_name,
        email=user_data.email,
        hashed_password=hashed_password,
    )
    return {"message": "Пользователь добавлен в бд"}
