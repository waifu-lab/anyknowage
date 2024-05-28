import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

from attrs import asdict
from bson import json_util
from db import get_mongodb, get_vectory
from fastapi import APIRouter, UploadFile, Response
from models.tempfile import Temp_File
from worker import ADD_knowledge

file_router = APIRouter()


@file_router.post("/upload")
async def upload_file(file: UploadFile):
    filedata = Temp_File(file)
    filedata_dict = json.loads(json_util.dumps(asdict(filedata)))
    ADD_knowledge.send(filedata_dict)
    return {"filename": file.filename}


@file_router.get("/files")
async def get_files():
    files = json.loads(json_util.dumps(get_mongodb().list_files()))
    return files


@file_router.get("/file_history")
async def get_file(pos: int):
    file = json.loads(json_util.dumps(get_mongodb().get_file_history(pos)))
    return file


@file_router.get("/file")
async def download_file(file_id: str) -> bytes:
    filedata = get_mongodb().get_file_from_id(file_id)
    file = get_mongodb().download_file(filedata["fsid"])
    header = {
        "Content-Disposition": f'attachment; filename={filedata["name"]+"."+filedata["ext"]}'
    }
    return Response(file, headers=header)


@file_router.delete("/file")
async def delete_file(file_id: str):
    filedata = get_mongodb().get_file_from_id(file_id)
    get_vectory().delete_documents(filedata["vector"])
    get_mongodb().delete_file(file_id)
    return {"file_id": file_id}
