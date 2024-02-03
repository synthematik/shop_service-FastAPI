from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from src.admin.auth import authentication_backend
from src.database import engine
from src.users.router import router as users_router
from src.auth.router import router as auth_router
from src.admin.models import UserAdmin, ProductsAdmin, CategoriesAdmin, ProductsImagesAdmin
from src.pages.router import router as pages_router
from src.shop.router import router as shop_router


app = FastAPI()

app.include_router(users_router)

app.include_router(auth_router)

app.include_router(pages_router)

app.include_router(shop_router)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)

admin.add_view(ProductsAdmin)

admin.add_view(CategoriesAdmin)

admin.add_view(ProductsImagesAdmin)

app.mount("/static", StaticFiles(directory="static"), name="static")
