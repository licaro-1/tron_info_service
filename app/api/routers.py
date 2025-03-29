from fastapi import APIRouter

from app.api.endpoints import tron_request_router

main_router = APIRouter()
main_router.include_router(tron_request_router, tags=["Tron Info"])
