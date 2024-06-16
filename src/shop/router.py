from fastapi import APIRouter
from src.shop.products.service import ProductsService, ImagesService


router = APIRouter(
    prefix="/shop"
)


@router.get("/products/")
async def get_products():
    products = await ProductsService.find_all()
    images = await ImagesService.find_all()
    return products, images
