from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import relationship

from src.database import Base


class Category(Base):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column("name", nullable=False, unique=True)

    products = relationship("Product", back_populates="category")

    def __str__(self):
        return f"{self.name}"
