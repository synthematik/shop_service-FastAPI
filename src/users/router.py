from fastapi import APIRouter
from src.users.service import UserService
from src.users.schemas import UserSchema
from typing import List, Optional

router = APIRouter(
    prefix="/profile",
    tags=["profile"]
)


@router.get("/{user_id}/")
async def get_profile(user_id: int) -> List[UserSchema]:
    return await UserService.find_one_by_id(user_id)
