from models.file import File
from modules.knowladge.basic import basic_file_parser
from util.logger import get_logger

logger = get_logger()


def parse_str(file: File):
    # TODO: 提取內部連結
    logger.info("📄 Starting text parsing")
    return basic_file_parser([file.get_Document(file.file)])
