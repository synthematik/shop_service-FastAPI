from fastapi import APIRouter, Depends
from src.users.service import UserService
from src.users.schemas import UserSchema
from typing import List
from src.users.models import Users
from src.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/profile",
    tags=["profile"]
)


@router.get("/{user_id}/")
async def get_profile_by_id(user: Users = Depends(get_current_user)) -> List[UserSchema]:
    return user


@router.get("/")
async def get_profile_by_email(email: str) -> List[UserSchema]:
    return await UserService.find_user_by_email(email)


