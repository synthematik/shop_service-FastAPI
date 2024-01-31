from fastapi import APIRouter, Depends, Response
from src.auth.schemas import RegisterSchema, LoginSchema
from src.users.service import UserService
from src.auth.exception import *
from src.auth.auth import get_password_hash, authenticate, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register/")
async def register_user(user_data: RegisterSchema):
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


@router.post("/login/")
async def login_user(response: Response, user_data: LoginSchema):
    user = await authenticate(user_data.email, user_data.password)
    if not user:
        raise UserNotExistsException()
    access_token = create_access_token({"sub": str(user[0].id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return {"access_token": access_token}

