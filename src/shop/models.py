from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Categories(Base):
    __tablename__ = 'categories'

    id = Column("id", Integer, primary_key=True)
    category_name = Column("category_name", String, nullable=False)

    products = relationship("Products", back_populates="category")

    def __str__(self):
        return f"{self.category_name}"


class Products(Base):
    __tablename__ = 'products'

    id = Column("id", Integer, primary_key=True)
    product_name = Column("product_name", String, nullable=False)
    product_price = Column("product_price", Integer, nullable=False)
    product_description = Column("product_description", String, nullable=False)
    image_id = Column("image_id", Integer)

    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Categories', back_populates='products')

    def __str__(self):
        return f"{self.product_name}"
