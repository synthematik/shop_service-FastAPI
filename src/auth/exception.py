from fastapi import HTTPException, status


class AuthException(HTTPException):
    status_code = 500
    default_detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.default_detail)


class UserAlreadyExistsException(AuthException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Пользователь с такой почтой уже существует"


class UserNotExistsException(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Неверная почта или пароль"


class TokenExpiredException(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Токен истек"


class TokenAbsentException(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Токен отсутствует"


class IncorrectTokenFormat(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Некорректный формат токена"


class UserIdNotFoundException(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED


class UserNotFoundException(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED
