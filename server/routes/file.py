from fastapi import APIRouter, UploadFile
from modules.knowladge.knowledge import add_knowledge
from db import mongodb, vectory
import json
from bson import json_util


file_router = APIRouter()


@file_router.post("/upload")
async def upload_file(file: UploadFile):
    add_knowledge(file)
    return {"filename": file.filename}


@file_router.get("/file")
async def get_file():
    files = json.loads(json_util.dumps(mongodb.list_files()))
    return files


@file_router.get("/vector")
async def list_vector():
    return vectory.count_documents()
