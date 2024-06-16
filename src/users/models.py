from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base


class User(Base):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column("name", nullable=False)
    last_name: Mapped[str] = mapped_column("last_name", nullable=False)
    email: Mapped[str] = mapped_column("email", nullable=False)
    hashed_password: Mapped[str] = mapped_column("hashed_password")

    orders = relationship("Order", back_populates="user")

    def __str__(self):
        return f"{self.email}"
