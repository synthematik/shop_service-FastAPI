from sqlalchemy import delete, insert, select
from typing import Optional

from src.database import async_session_maker


class BaseService:
    model = None

    @classmethod
    async def find_one_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            smt = insert(cls.model).values(**data)
            await session.execute(smt)
            await session.commit()
