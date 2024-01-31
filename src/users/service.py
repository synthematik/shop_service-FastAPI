from sqlalchemy import select, insert

from src.database import async_session_maker
from src.service.base import BaseService
from src.users.models import Users


class UserService(BaseService):
    model = Users

    @classmethod
    async def find_user_by_email(cls, email: str):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(email=email)
            result = await session.execute(query)
            return result.mappings().all()
