from datetime import datetime
from uuid import UUID, uuid4

import bson
import gridfs
import pymongo
import pytz
from haystack.dataclasses import Document


class Mongodb:
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb://admin:password@localhost:27017",
            connect=False,
        )
        # drop all data in anyknowledge database
        # self.client.anyknowledge.files.drop()
        # self.client.anyknowledge.tempfiles.drop()
        # db = self.client.anyknowledge
        # fs = gridfs.GridFS(db)
        # for file in fs.find():
        #     fs.delete(file._id)

    def get_file_sha1(self, sha1: str) -> str:
        db = self.client.anyknowledge
        file = db.files.find_one({"sha1": sha1})
        return file

    def add_file(
        self,
        file_id: UUID,
        file: bytes,
        sha1: str,
        name: str,
        ext: str,
        vector: list[Document],
        context: str = None,
    ) -> None:
        db = self.client.anyknowledge
        fs = gridfs.GridFS(db)
        fsid = fs.put(file)
        db.files.insert_one(
            {
                "file_id": str(file_id),
                "sha1": sha1,
                "fsid": fsid,
                "name": name,
                "ext": ext,
                "vectoe_ids": [vector_id.id for vector_id in vector],
                "time": datetime.now(pytz.utc),
                "context": context,
            }
        )

    def delete_file(self, file_id: UUID) -> None:
        db = self.client.anyknowledge
        file = db.files.find_one({"file_id": str(file_id)})
        fs = gridfs.GridFS(db)
        fs.delete(file.get("fsid"))
        db.files.delete_one({"file_id": str(file_id)})

    def list_files(self) -> dict:
        db = self.client.anyknowledge
        files = db.files.find()
        return files

    def get_file_from_id(self, file_id: UUID) -> dict:
        db = self.client.anyknowledge
        file = db.files.find_one({"file_id": str(file_id)})
        return file

    def download_file(self, file_id: UUID) -> bytes:
        db = self.client.anyknowledge
        file = db.files.find_one({"file_id": str(file_id)})
        fs = gridfs.GridFS(db)
        file = fs.get(file.get("fsid"))
        return file.read()

    def get_file_history(self, pos: int = 0) -> dict:
        db = self.client.anyknowledge
        files = db.files.find().skip(pos).limit(20)
        return files

    def add_temp_file(self, file: bytes) -> str:
        db = self.client.anyknowledge
        fs = gridfs.GridFS(db)
        fsid = fs.put(file)
        id = db.tempfiles.insert_one(
            {
                "fsid": fsid,
            }
        )
        return str(id.inserted_id)

    def get_tempfile(self, file_id: str) -> bytes:
        db = self.client.anyknowledge
        fsid = db.tempfiles.find_one({"_id": bson.ObjectId(file_id)}).get("fsid")
        fs = gridfs.GridFS(db)
        file = fs.get(fsid)
        return file.read()

    def delete_tempfile(self, file_id: str) -> None:
        db = self.client.anyknowledge
        fsid = db.tempfiles.find_one({"_id": bson.ObjectId(file_id)}).get("fsid")
        fs = gridfs.GridFS(db)
        fs.delete(fsid)
        db.tempfiles.delete_one({"_id": bson.ObjectId(file_id)})

    def get_chat_history(self, pos: int = 0) -> dict:
        db = self.client.anyknowledge
        chats = db.chats.find().sort({"_id": -1}).skip(pos).limit(20)
        return [{**chat, "_id": str(chat["_id"])} for chat in chats]

    def add_chat(self, ask: str, answer: dict) -> None:
        db = self.client.anyknowledge
        db.chats.insert_one(
            {
                "chat_id": str(uuid4()).split("-")[0],
                "ask": ask,
                "answer": answer,
                "time": datetime.now(),
            }
        )

    def delete_chat(self, chat_id: str) -> None:
        db = self.client.anyknowledge
        db.chats.delete_one({"chat_id": chat_id})
