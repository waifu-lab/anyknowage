from fastapi import APIRouter, UploadFile
from db import get_mongodb, get_vectory
import json
from bson import json_util
from worker import ADD_knowledge
from models.tempfile import Temp_File
from attrs import asdict

file_router = APIRouter()


@file_router.post("/upload")
async def upload_file(file: UploadFile):
    filedata = Temp_File(file)
    filedata_dict = json.loads(json_util.dumps(asdict(filedata)))
    print(filedata_dict)
    ADD_knowledge.send(filedata_dict)
    return {"filename": file.filename}


@file_router.get("/file")
async def get_file():
    files = json.loads(json_util.dumps(get_mongodb().list_files()))
    return files


@file_router.get("/vector")
async def list_vector():
    return get_vectory().count_documents()
