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

    id = Column("id", Integer, primary_key=True, index=True)
    product_name = Column("product_name", String, nullable=False)
    product_price = Column("product_price", Integer, nullable=False)
    product_description = Column("product_description", String, nullable=False)

    images = relationship('ProductImages', back_populates='product')

    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Categories', back_populates='products')

    def __str__(self):
        return f"{self.product_name}"


class ProductImages(Base):
    __tablename__ = 'product_images'

    id = Column(Integer, primary_key=True)
    image_url = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))

    product = relationship('Products', back_populates='images')


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
