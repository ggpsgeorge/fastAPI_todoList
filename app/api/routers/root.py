from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message":"Hell, World!"}

@router.get("/info")
async def read_info():
    return {"secret_key": settings.secret_key}