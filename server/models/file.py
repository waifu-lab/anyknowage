from typing import Optional
from attrs import define
from haystack.dataclasses import Document
from uuid import uuid4
import hashlib


@define
class File:
    name: str = None
    size: int = None
    hash: str = None
    file: bytes | str = None
    file_ext: str = None
    url: Optional[str] = None
    document: Optional[Document] = None
    loader: Optional[callable] = None
    uuid = uuid4()

    def __init__(self, name: str, file: bytes | str, ext: str = ".txt") -> None:
        self.name = name
        self.file = file
        self.size = len(file)
        self.file_ext = ext

    def is_null(self) -> bool:
        return self.size == 0

    def get_sha1(self) -> str:
        if isinstance(self.file, str):
            self.hash = hashlib.sha1(self.file.encode()).hexdigest()
        else:
            self.hash = hashlib.sha1(self.file).hexdigest()
        return self.hash

    def get_Document(self, text: str) -> Document:
        self.document = Document(
            content=text,
            meta={"title": self.name},
        )
        return self.document

    def add_meta_to_document(self, meta=None) -> Document:
        if self.document:
            defaut_meta = {"title": self.name}
            if meta:
                defaut_meta.update(meta)
            self.document.meta.update(defaut_meta)
        return self.document

    def run(self) -> dict:
        if self.loader:
            doc = self.loader(self)
        return doc
