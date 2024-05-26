from fastapi import APIRouter
from models.ai_models import GPT_Request
from modules.chat.gpt import GPT

chat_router = APIRouter()


@chat_router.post("/chat")
async def new_chat(request: GPT_Request):
    print(request)
    rt = GPT(request.model).ASK(request.question)
    print(rt)
    return rt
