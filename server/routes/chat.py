from fastapi import APIRouter, UploadFile


chat_router = APIRouter()


@chat_router.post("/chat")
async def new_chat():
    ...
