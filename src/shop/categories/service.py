from src.service.base import BaseService
from src.shop.categories.models import Category


class CategoriesService(BaseService):
    model = Category
