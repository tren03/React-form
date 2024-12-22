from fastapi import APIRouter, FastAPI, Request

from backend.auth.auth import router as auth_router
from backend.crud.crud import router as crud_router

router = APIRouter()


router.include_router(crud_router, prefix="/crud", tags=["crud operations"])
router.include_router(auth_router, prefix="/auth", tags=["auth operations"])
