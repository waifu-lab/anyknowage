from loguru import logger
from fastapi import UploadFile

from models.file import File
from urllib.parse import urlparse

from modules.knowladge.strtext import parse_str
from modules.knowladge.textfiles import parse_txt, parse_pdf, parse_docx, parse_markdown
from modules.knowladge.url import parse_url
from db import mongodb, vectory
from haystack.document_stores.types import DuplicatePolicy

ext_to_parser = {
    "txt": parse_txt,
    "pdf": parse_pdf,
    "docx": parse_docx,
    "md": parse_markdown,
}


def is_url(url: str) -> bool:
    try:
        url = urlparse(str(url))
        return all([url.scheme, url.netloc])
    except ValueError:
        return False


def add_knowledge(data: UploadFile | str):
    """
    檢查各類條件
    做好前處理
    """

    if isinstance(data, str):
        file = File(name="text", file=data)
    else:
        file = File(
            name=data.filename, file=data.file.read(), ext=data.filename.split(".")[-1]
        )
    file.get_sha1()
    logger.info(f"File {file.name} has been hashed")
    logger.debug(file.hash)

    if file.is_null():
        logger.error("File is empty")
        return

    if mongodb.get_file_sha1(file.hash):
        logger.error("File already exists")
        return

    if isinstance(data, str):
        if is_url(data):
            file.loader = parse_url
        else:
            file.loader = parse_str
    else:
        if file.name.split(".")[-1] in ext_to_parser:
            file.loader = ext_to_parser.get(file.name.split(".")[-1])
        else:
            logger.error("File type not supported")
            return

    embedding = file.run()
    logger.debug(embedding)
    mongodb.add_file(
        file.uuid,
        file.file,
        file.hash,
        file.name,
        file.file_ext,
        embedding["documents"],
    )
    vectory.write_documents(embedding["documents"], policy=DuplicatePolicy.OVERWRITE)
