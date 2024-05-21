from fastapi import APIRouter, UploadFile
from modules.knowladge.knowledge import add_knowledge
from db import mongodb

file_router = APIRouter()


@file_router.post("/upload")
async def upload_file(file: UploadFile):
    add_knowledge(file)
    return {"filename": file.filename}


@file_router.get("/file")
async def get_file():
    return mongodb.list_files()
