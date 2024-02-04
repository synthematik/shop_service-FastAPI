from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
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
