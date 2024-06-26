import re

from models.file import File
from modules.crawler import Crawer, Github, Gitlab, twitter
from modules.knowladge.basic import basic_file_parser
from util.logger import get_logger

logger = get_logger()
special_urls = {
    "github.com": Github,
    "gitlab.com": Gitlab,
    "x.com": twitter,
    "twitter.com": twitter,
}


def parse_url(file: File):
    logger.info("🌐  Starting web crawing")
    domain = re.match(r"https?:\/\/((www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256})", file.file)[
        1
    ]
    if domain in special_urls:
        data = special_urls[domain](file.file).get()
    else:
        try:
            data = Crawer(file.file).get()
        except Exception as e:
            logger.error(e)
            return None
    if data is None:
        return None
    doc = file.get_Document(data["Content"])
    file.add_meta_to_document(data["Meta"])
    return basic_file_parser([doc])
