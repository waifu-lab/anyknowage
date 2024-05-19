from .basic import basic_file_parser
from models.file import File


def parse_txt(file: File):
    text = file.file.decode("utf-8")
    return basic_file_parser([file.get_Document(text)])


def parse_pdf(file: File):
    basic_file_parser()


def parse_docx(file: File):
    basic_file_parser()


def parse_markdown(file: File):
    basic_file_parser()
