from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from src.database import Base


class Product(Base):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column("name", nullable=False)
    price: Mapped[int] = mapped_column("price", nullable=False)
    description: Mapped[str] = mapped_column("description", nullable=False)
    quantity: Mapped[int] = mapped_column("quantity", nullable=False)

    images = relationship('ProductImage', back_populates='product')

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    category = relationship('Category', back_populates='products')

    orders = relationship('Order', back_populates='product')

    def __str__(self):
        return f"{self.name}"


class ProductImage(Base):
    __tablename__ = 'product_images'

    url: Mapped[str] = mapped_column(nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))

    product = relationship('Product', back_populates='images')
