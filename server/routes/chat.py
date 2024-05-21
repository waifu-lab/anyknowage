from fastapi import APIRouter
from models.ai_models import GPTModel
from modules.chat.gpt import GPT

chat_router = APIRouter()


@chat_router.post("/chat")
async def new_chat(model: str, question: str):
    gpt = GPTModel(model=model)
    rt = GPT(gpt).ASK(question)
    print(rt)
    return rt
