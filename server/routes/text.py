from fastapi import APIRouter
from worker import ADD_knowledge
from pydantic import BaseModel

text_router = APIRouter()


class text_req(BaseModel):
    text: str


@text_router.post("/text")
async def upload_text(text: text_req):
    ADD_knowledge.send(text.text)
    return {"text": text.text}
