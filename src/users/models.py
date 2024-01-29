from sqlalchemy import Integer, String, Column
from src.database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column("id", Integer, primary_key=True, index=True)
    name = Column("name", String, nullable=False)
    last_name = Column("last_name", String, nullable=False)
    email = Column("email", String, nullable=False)
    hashed_password = Column("hashed_password", String)
