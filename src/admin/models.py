from sqladmin import ModelView

from src.users.models import Users


class UserAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email, Users.name, Users.last_name]
    name_plural = "Пользователи"
    name = "Пользователь"
    icon = "fa-solid fa-user"
    column_details_exclude_list = [Users.hashed_password]
