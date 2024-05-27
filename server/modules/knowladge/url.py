from modules.knowladge.basic import basic_file_parser
from models.file import File
from modules.crawer import Crawer, Github, Gitlab, twitter
import re

special_urls = {
    "github.com": Github,
    "gitlab.com": Gitlab,
    "x.com": twitter,
    "twitter.com": twitter,
}


def parse_url(file: File):
    domain = re.match(r"https?:\/\/((www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256})", file.file)[
        1
    ]
    if domain in special_urls:
        data = special_urls[domain](file.file).get()
    else:
        data = Crawer(file.file).get()
    if data is None:
        return

    file.add_meta_to_document(data["Meta"])
    basic_file_parser([file.get_Document(data["Content"])])
