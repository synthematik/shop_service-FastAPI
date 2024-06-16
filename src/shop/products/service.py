from src.service.base import BaseService
from src.shop.products.models import Product, ProductImage


class ProductsService(BaseService):
    model = Product


class ImagesService(BaseService):
    model = ProductImage
