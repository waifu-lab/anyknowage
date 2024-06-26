from pathlib import Path

from haystack.components.converters import PyPDFToDocument
from haystack.components.preprocessors import DocumentCleaner, DocumentSplitter
from haystack.dataclasses import Document
from haystack_integrations.components.embedders.fastembed import (
    FastembedDocumentEmbedder,
    FastembedTextEmbedder,
)
from ckip_transformers.nlp import CkipWordSegmenter
from opencc import OpenCC
import re

from util.logger import get_logger

logger = get_logger()
cleaner = DocumentCleaner()
splitter = DocumentSplitter(split_by="word", split_length=100)
document_embedder = FastembedDocumentEmbedder(
    model="intfloat/multilingual-e5-large",
    parallel=0,
    prefix="query:",
)


def pdf_parser(file: Path):
    converter = PyPDFToDocument()
    docs = converter.run(sources=[file])
    return basic_file_parser(docs["documents"])


def basic_file_parser(text: list[Document]):
    logger.info("</> Embedding text...")

    def is_chinese(text):
        return re.search("[\u4e00-\u9fff]", text) is not None

    if is_chinese(text[0].content):
        logger.info("Chinese text detected")
        converter = OpenCC("s2t")
        chtext = converter.convert(text[0].content)
        ws_driver = CkipWordSegmenter(model="bert-base")
        ws = ws_driver([chtext])
        text[0].content = " ".join(ws[0])

    splitted_docs = splitter.run(cleaner.run(text)["documents"])
    document_embedder.meta_fields_to_embed = text[0].meta.keys()
    logger.info("🔥 Warming up the embedder")
    document_embedder.warm_up()
    documents_with_embeddings = document_embedder.run(splitted_docs["documents"])
    logger.info("🎉 Finished embedding text")
    return documents_with_embeddings


# def basic_text_parser(text: str):
#     text_embedder = FastembedTextEmbedder(
#         model="intfloat/multilingual-e5-large",
#         parallel=0,
#         prefix="query:",
#     )
#     text_embedder.warm_up()
#     text_emnedding = text_embedder.run(text)
#     return text_emnedding
