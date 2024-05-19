import pymongo
import gridfs
import bson
from uuid import UUID


class Mongodb:
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb://admin:password@localhost:27017",
            connect=False,
        )

    def get_file_sha1(self, sha1: str) -> str:
        db = self.client.anyknowledge
        file = db.files.find_one({"sha1": sha1})
        return file

    def add_file(
        self, file_id: UUID, file: bytes, sha1: str, name: str, ext: str
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
            }
        )
