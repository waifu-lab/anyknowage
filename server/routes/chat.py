from db import get_mongodb
from fastapi import APIRouter
from models.ai_models import GPT_Request
from modules.chat.gpt import GPT
from haystack.dataclasses import ExtractedAnswer
import json

chat_router = APIRouter()


@chat_router.post("/chat")
async def new_chat(request: GPT_Request):
    rt: ExtractedAnswer = GPT(
        request.model, maxtoken=request.maxtoken, key=request.token
    ).ASK(request.question)
    docs = []
    for answer in rt["reader"]["answers"]:
        docs.append(
            {
                "answer": answer.query,
                "data": answer.data,
                "context": answer.document.content if answer.document else None,
                "doc_id": answer.document.id if answer.document else None,
            }
        )
    answer = rt["generator"]["replies"][0]
    get_mongodb().add_chat(
        request.question,
        {
            "answer": answer,
            "docs": docs,
        },
    )
    return rt


@chat_router.delete("/chat")
async def delete_chat(chat_id: str):
    get_mongodb().delete_chat(chat_id)
    return {"status": "ok"}


@chat_router.get("/chats")
async def get_chats(pos: int = 0):
    return get_mongodb().get_chat_history(pos)
