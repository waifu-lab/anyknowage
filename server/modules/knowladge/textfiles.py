from modules.knowladge.basic import basic_file_parser, pdf_parser
from models.file import File
from tempfile import NamedTemporaryFile
import pypandoc
from pathlib import Path
from util.readme_unmark import unmark
import os
from loguru import logger


def parse_txt(file: File):
    logger.info("📄 Starting text file parsing")
    text = file.file.decode("utf-8")
    return basic_file_parser([file.get_Document(text)])


def parse_pdf(file: File):
    logger.info("📄 Starting pdf file parsing")
    with NamedTemporaryFile(delete=False) as temp:
        temp.write(file.file)
        temp_path = Path(temp.name)
    try:
        result = pdf_parser(temp_path)
    finally:
        os.remove(temp_path)
    return result


def parse_docx(file: File):
    logger.info("📄 Starting docx file parsing")
    with NamedTemporaryFile(delete=False) as temp:
        temp.write(file.file)
        temp_path = Path(temp.name)
    try:
        text = pypandoc.convert_file(temp_path, "textfile", format="docx")
    finally:
        os.remove(temp_path)
    return basic_file_parser([file.get_Document(text)])


def parse_markdown(file: File):
    logger.info("📄 Starting markdown file parsing")
    text = file.file.decode("utf-8")
    text = unmark(text)
    return basic_file_parser([file.get_Document(text)])
