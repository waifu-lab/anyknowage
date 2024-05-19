from fastapi import APIRouter, UploadFile
from modules.knowladge.knowledge import add_knowledge

file_router = APIRouter()


@file_router.post("/upload")
async def upload_file(file: UploadFile):
    add_knowledge(file)
    return {"filename": file.filename}
