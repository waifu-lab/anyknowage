import os
from pathlib import Path
from tempfile import NamedTemporaryFile

from haystack.components.audio import LocalWhisperTranscriber

from models.file import File
from modules.knowladge.basic import basic_file_parser
from util.logger import get_logger

logger = get_logger()


def video_file_parser(file: File):
    # not support video, only read sound
    logger.info("🎞️ Starting video file parsing")
    with NamedTemporaryFile(delete=False) as temp:
        temp.write(file.file)
        temp_path = Path(temp.name)
    try:
        whisper = LocalWhisperTranscriber(model="small")
        whisper.warm_up()
        transcription = whisper.run(sources=[temp_path])
        text = transcription["documents"]
        file.document = text[0]
        text[0] = file.add_meta_to_document()
    finally:
        os.remove(temp_path)
    return basic_file_parser(text)
