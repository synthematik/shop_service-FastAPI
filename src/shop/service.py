from src.service.base import BaseService
from src.shop.models import Categories, Products, ProductImages


class CategoriesService(BaseService):
    model = Categories


class ProductsService(BaseService):
    model = Products


class ImagesService(BaseService):
    model = ProductImages
