from loguru import logger
from haystack.dataclasses import Document
from haystack.components.preprocessors import DocumentCleaner, DocumentSplitter
from haystack_integrations.components.embedders.fastembed import FastembedDocumentEmbedder
from haystack.document_stores.types import DuplicatePolicy


def basic_file_parser(file):
    cleaner = DocumentCleaner()
    splitter = DocumentSplitter(split_by='sentence', split_length=3)
    splitted_docs = splitter.run(cleaner.run(file)["documents"])
    document_embedder = FastembedDocumentEmbedder(model="BAAI/bge-small-en-v1.5", parallel = 0, meta_fields_to_embed=["title"])
    document_embedder.warm_up()
    documents_with_embeddings = document_embedder.run(splitted_docs["documents"])
    vectory.write_documents(documents_with_embeddings.get("documents"), policy=DuplicatePolicy.OVERWRITE)

if __name__ == "__main__":
    import sys
    sys.path.append(r"C:\Users\phill\OneDrive\Documents\coed_thing\anyknowage\server")
    from db import vectory
    with open(r"C:\Users\phill\OneDrive\Documents\coed_thing\anyknowage\server\readme_EN.txt", "r") as file:
        file = file.read()
    basic_file_parser([Document(content=file, meta={"title": "readme_EN.txt"})])