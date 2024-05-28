from fastapi import APIRouter
from models.ai_models import GPT_Request
from modules.chat.gpt import GPT
from db import get_mongodb

chat_router = APIRouter()


@chat_router.post("/chat")
async def new_chat(request: GPT_Request):
    rt = GPT(request.model).ASK(request.question)
    get_mongodb().add_chat(request.question, rt)
    return rt
