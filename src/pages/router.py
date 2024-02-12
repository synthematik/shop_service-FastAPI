from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from src.shop.service import *


router = APIRouter(
    prefix="/pages",
    tags=["Front"]
)

templates = Jinja2Templates(directory="templates/")


@router.get("/")
async def index(request: Request):
    products = await ProductsService.find_all()
    images = await ImagesService.find_all()
    return templates.TemplateResponse("index_app.html", {"request": request, "products": products, "images": images})


@router.post("/register/", name='login', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("auth/register_user.html", {"request": request})


@router.post("/login/")
async def login(request: Request):
    return templates.TemplateResponse("auth/login_user.html", {"request": request})
