from fastapi import APIRouter

text_router = APIRouter()


@text_router.get("/text")
async def upload_text():
    ...
