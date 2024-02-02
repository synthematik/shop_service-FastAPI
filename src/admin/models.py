from sqladmin import ModelView

from src.users.models import Users
from src.shop.models import Categories, Products


class UserAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email, Users.name, Users.last_name]
    name_plural = "Пользователи"
    name = "Пользователь"
    icon = "fa-solid fa-user"
    column_details_exclude_list = [Users.hashed_password]


class CategoriesAdmin(ModelView, model=Categories):
    column_list = [Categories.id, Categories.category_name, Categories.products]
    name_plural = "Категории"
    name = "Категория"
    icon = "fa-solid"


class ProductsAdmin(ModelView, model=Products):
    column_list = [
        Products.id,
        Products.product_name,
        Products.product_price,
        Products.product_description,
        Products.category,
        Products.category_id
    ]
    name_plural = "Продукты"
    name = "Продукт"
    icon = "fa-solid"
