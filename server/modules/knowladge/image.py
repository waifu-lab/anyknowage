import os
from pathlib import Path
from tempfile import NamedTemporaryFile

from loguru import logger
from models.file import File
from modules.knowladge.basic import basic_file_parser


def image_file_parser(file: File):
    logger.info("🖼️ Starting image file parsing")
    with NamedTemporaryFile(delete=False) as temp:
        temp.write(file.file)
        temp_path = Path(temp.name)
    try:
        # TODO:
        text = ...
    finally:
        os.remove(temp_path)
    return basic_file_parser([file.get_Document(text)])
