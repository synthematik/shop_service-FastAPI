from sqladmin import ModelView

from src.users.models import User
from src.shop.products.models import Product, ProductImage
from src.shop.orders.models import Order
from src.shop.categories.models import Category


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.name, User.last_name]
    name_plural = "Пользователи"
    name = "Пользователь"
    icon = "fa-solid fa-user"
    column_details_exclude_list = [User.hashed_password]


class CategoriesAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name, Category.products]
    name_plural = "Категории"
    name = "Категория"
    icon = "fa-solid fa-list"


class ProductsAdmin(ModelView, model=Product):
    column_list = [
        Product.id,
        Product.name,
        Product.price,
        Product.description,
        Product.category,
        Product.category_id,
    ]
    name_plural = "Продукты"
    name = "Продукт"
    icon = "fa-solid"


class ProductsImagesAdmin(ModelView, model=ProductImage):
    column_list = [
        ProductImage.id,
        ProductImage.url,
        ProductImage.product_id,
        ProductImage.product
    ]
    name_plural = "Изображения"
    name = "Изображение"
    icon = "fa-solid fa-image"


class OrdersAdmin(ModelView, model=Order):
    column_list = [
        Order.id,
        Order.product_id,
        Order.user_id
    ]
    name_plural = "Заказы"
    name = "Заказ"
    icon = "fa-solid fa-orders"
