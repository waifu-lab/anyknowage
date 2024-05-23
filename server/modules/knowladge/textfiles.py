from .basic import basic_file_parser
from models.file import File
from tempfile import TemporaryFile
import pypandoc


def parse_txt(file: File):
    text = file.file.decode("utf-8")
    return basic_file_parser([file.get_Document(text)])


def parse_pdf(file: File):
    with TemporaryFile() as temp:
        temp.write(file.file)
        temp.seek(0)
        text = pypandoc.convert_file(temp, "txt", format="pdf")
    return basic_file_parser([file.get_Document(text)])


def parse_docx(file: File):
    with TemporaryFile() as temp:
        temp.write(file.file)
        temp.seek(0)
        text = pypandoc.convert_file(temp, "txt", format="docx")
    return basic_file_parser([file.get_Document(text)])


def parse_markdown(file: File):
    text = file.file.decode("utf-8")
    return basic_file_parser([file.get_Document(text)])
