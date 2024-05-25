from modules.knowladge.basic import basic_file_parser, pdf_parser
from models.file import File
from tempfile import NamedTemporaryFile
import pypandoc
from markdown import Markdown
from io import StringIO
from pathlib import Path
import os


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False


def unmark(text):
    return __md.convert(text)


def parse_txt(file: File):
    text = file.file.decode("utf-8")
    return basic_file_parser([file.get_Document(text)])


def parse_pdf(file: File):
    with NamedTemporaryFile(delete=False) as temp:
        temp.write(file.file)
        temp_path = Path(temp.name)
    try:
        result = pdf_parser(temp_path)
    finally:
        os.remove(temp_path)
    return result


def parse_docx(file: File):
    with NamedTemporaryFile(delete=False) as temp:
        temp.write(file.file)
        temp_path = Path(temp.name)
    try:
        text = pypandoc.convert_file(temp_path, "textfile", format="docx")
    finally:
        os.remove(temp_path)
    return basic_file_parser([file.get_Document(text)])


def parse_markdown(file: File):
    text = file.file.decode("utf-8")
    text = unmark(text)
    return basic_file_parser([file.get_Document(text)])
