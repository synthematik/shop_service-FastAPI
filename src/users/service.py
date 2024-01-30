from src.service.base import BaseService
from src.users.models import Users


class UserService(BaseService):
    model = Users
