from loguru import logger
from fastapi import UploadFile

from models.file import File
from models.tempfile import Temp_File
from urllib.parse import urlparse

from modules.knowladge.strtext import parse_str
from modules.knowladge.textfiles import parse_txt, parse_pdf, parse_docx, parse_markdown
from modules.knowladge.url import parse_url
from modules.knowladge.audio import audio_file_parser
from modules.knowladge.video import video_file_parser
from modules.knowladge.image import image_file_parser

from db import get_mongodb, get_vectory
from haystack.document_stores.types import DuplicatePolicy
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
import io

ext_to_parser = {
    "txt": parse_txt,
    "pdf": parse_pdf,
    "docx": parse_docx,
    "md": parse_markdown,
    "mp3": audio_file_parser,
    "mp4": video_file_parser,
    # "jpg": image_file_parser,
    # "jpeg": image_file_parser,
    # "png": image_file_parser,
}


def is_url(url: str) -> bool:
    try:
        url = urlparse(str(url))
        return all([url.scheme, url.netloc])
    except ValueError:
        return False


def add_knowledge(data: dict | str):
    """
    檢查各類條件
    做好前處理
    """

    if isinstance(data, str):
        file = File(name="text", file=data)
        file.istext = True
    else:
        print(data)
        filebytes = get_mongodb().get_tempfile(data["file_id"])
        file = File(name=data["name"], file=filebytes, ext=data["ext"])
    file.get_sha1()
    logger.info(f"File {file.name} has been hashed")
    logger.debug(file.hash)

    if file.is_null():
        logger.error("File is empty")
        return

    if get_mongodb().get_file_sha1(file.hash):
        logger.error("File already exists")
        return

    if file.istext:
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
    if embedding is None:
        logger.error("File is empty")
        return
    if embedding["documents"] == []:
        logger.error("File has no content")
        return
    logger.debug(embedding)
    if file.istext:
        tmp = io.BytesIO()
        tmp.write(file.file.encode())
        tmp.seek(0)
        file.file = tmp

    get_mongodb().add_file(
        file.uuid,
        file.file,
        file.hash,
        file.name,
        file.file_ext,
        embedding["documents"],
    )
    get_vectory().write_documents(
        embedding["documents"], policy=DuplicatePolicy.OVERWRITE
    )
