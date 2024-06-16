from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from src.admin.auth import authentication_backend
from src.database import engine
from src.users.router import router as users_router
from src.auth.router import router as auth_router
from src.admin.models import UserAdmin, ProductsAdmin, CategoriesAdmin, ProductsImagesAdmin, OrdersAdmin
from src.shop.router import router as shop_router


app = FastAPI()

app.include_router(users_router)

app.include_router(auth_router)

app.include_router(shop_router)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)

admin.add_view(ProductsAdmin)

admin.add_view(CategoriesAdmin)

admin.add_view(ProductsImagesAdmin)

admin.add_view(OrdersAdmin)

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.mount("/static", StaticFiles(directory="static"), name="static")
