from attrs import define
from db import get_mongodb
from fastapi import UploadFile


@define
class Temp_File:
    name: str = None
    file_id: str = None
    ext: str = None

    def __init__(self, file: UploadFile) -> None:
        if file is None:
            raise ValueError("file is empty")
        self.name = file.filename
        self.ext = file.filename.split(".")[-1]
        self.__send_to_mongo(file.file.read())

    def __send_to_mongo(self, file: bytes) -> None:
        self.file_id = get_mongodb().add_temp_file(file)
