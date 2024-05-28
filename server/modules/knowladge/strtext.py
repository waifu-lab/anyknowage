from modules.knowladge.basic import basic_file_parser
from models.file import File


def parse_str(file: File):
    # TODO: 提取內部連結
    return basic_file_parser([file.get_Document(file.file)])
