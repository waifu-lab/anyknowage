from db.mongo.mongodb import Mongodb
from db.vector.vector_storage import Qdrant

vectory = None
mongodb = None


def get_vectory():
    global vectory
    if vectory is None:
        vectory = Qdrant().document_store
    return vectory


def get_mongodb():
    global mongodb
    if not mongodb:
        mongodb = Mongodb()
    return mongodb
