from fastapi import FastAPI
from sqladmin import Admin

from src.admin.auth import authentication_backend
from src.database import engine
from src.users.router import router as users_router
from src.auth.router import router as auth_router
from src.admin.models import UserAdmin

app = FastAPI()

app.include_router(users_router)

app.include_router(auth_router)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)
