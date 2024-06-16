from src.service.base import BaseService
from src.shop.orders.models import Order


class OrdersService(BaseService):
    model = Order
