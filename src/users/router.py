from fastapi import APIRouter
from src.users.service import UserService
from src.users.schemas import UserSchema
from typing import List

router = APIRouter(
    prefix="/profile",
    tags=["profile"]
)


@router.get("/{user_id}/")
async def get_profile_by_id(user_id: int) -> List[UserSchema]:
    return await UserService.find_one_by_id(user_id)


@router.get("/")
async def get_profile_by_email(email: str) -> List[UserSchema]:
    return await UserService.find_user_by_email(email)


