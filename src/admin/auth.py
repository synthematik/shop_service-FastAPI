from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from src.auth.auth import authenticate, create_access_token
from src.auth.dependencies import get_current_user
from src.config import settings


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]

        user = await authenticate(email=email, password=password)
        if user:
            access_token = create_access_token({"sub": str(user[0].id)})
            request.session.update({"token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        user = await get_current_user(token)

        if not user:
            return False

        return True


authentication_backend = AdminAuth(secret_key=settings.SECRET_KEY)
