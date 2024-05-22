from fastapi import APIRouter
from models.ai_models import GPTModel
from modules.chat.gpt import GPT

chat_router = APIRouter()


@chat_router.post("/chat")
async def new_chat(model: str, question: str):
    try:
        gpt = GPTModel(model=model)
    except ValueError:
        return {"error": f"{model} cannot be found."}
    rt = GPT(gpt).ASK(question)
    print(rt)
    return rt
