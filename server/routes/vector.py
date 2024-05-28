from db import get_vectory
from fastapi import APIRouter

vector_router = APIRouter()


@vector_router.get("/vector")
async def list_vector():
    return get_vectory().count_documents()
