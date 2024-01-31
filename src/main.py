from fastapi import FastAPI

from src.users.router import router as users_router
from src.auth.router import router as auth_router


app = FastAPI()

app.include_router(users_router)

app.include_router(auth_router)