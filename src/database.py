from sqlalchemy import TIMESTAMP, func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm import mapped_column, Mapped

from src.config import settings

DATABASE_URL = settings.get_database_url()

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    created_at = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = mapped_column(TIMESTAMP(timezone=True), onupdate=func.now())
