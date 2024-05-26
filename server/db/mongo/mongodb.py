import pymongo
import gridfs
import bson
from uuid import UUID
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
    ) -> None:
        db = self.client.anyknowledge
        fs = gridfs.GridFS(db)
        fsid = fs.put(file)
        db.files.insert_one(
            {
                "file_id": bson.Binary.from_uuid(file_id),
                "sha1": sha1,
                "fsid": fsid,
                "name": name,
                "ext": ext,
                "vectoe_ids": [vector_id.id for vector_id in vector],
            }
        )

    def list_files(self) -> dict:
        db = self.client.anyknowledge
        files = db.files.find()
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
        print(id)
        return str(id.inserted_id)

    def get_tempfile(self, file_id: str) -> bytes:
        db = self.client.anyknowledge
        fsid = db.tempfiles.find_one({"_id": bson.ObjectId(file_id)}).get("fsid")
        fs = gridfs.GridFS(db)
        print(fsid)
        file = fs.get(fsid)
        return file.read()
