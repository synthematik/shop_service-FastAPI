from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database import Base


class Order(Base):

    __tablename__ = 'orders'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=False)

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")
