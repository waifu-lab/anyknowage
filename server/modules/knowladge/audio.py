from modules.knowladge.basic import basic_file_parser
from models.file import File
from tempfile import NamedTemporaryFile
from pathlib import Path
import os
from haystack.components.audio import LocalWhisperTranscriber
from loguru import logger


# only run on linux
def audio_file_parser(file: File):
    logger.info("🎵 Starting audio file parsing")
    with NamedTemporaryFile(delete=False) as temp:
        temp.write(file.file)
        temp_path = Path(temp.name)
    try:
        logger.info("🔥 Warming up the LocalWhisperTranscriber")
        whisper = LocalWhisperTranscriber(model="small")
        whisper.warm_up()
        logger.info("🏃 Running the LocalWhisperTranscriber")
        transcription = whisper.run(sources=[temp_path])
        text = transcription["documents"]
        file.document = text[0]
        text[0] = file.add_meta_to_document()
    except Exception as e:
        logger.error(f"❌ Error occurred during audio file parsing: {e}")
    finally:
        os.remove(temp_path)
    logger.info("🎉 Finished audio file parsing")
    return basic_file_parser(text)
