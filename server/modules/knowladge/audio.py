from modules.knowladge.basic import basic_file_parser
from models.file import File
from tempfile import NamedTemporaryFile
from pathlib import Path
import os


def audio_file_parser(file: File):
    with NamedTemporaryFile(delete=False) as temp:
        temp.write(file.file)
        temp_path = Path(temp.name)
    try:
        # TODO:
        text = ...
    finally:
        os.remove(temp_path)
    return basic_file_parser([file.get_Document(text)])
