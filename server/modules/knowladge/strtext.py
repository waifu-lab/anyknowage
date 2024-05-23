from .basic import basic_text_parser
from models.file import File


def parse_str(file: File):
    # TODO: 提取內部連結
    return basic_text_parser(file.file)
