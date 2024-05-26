from db.vector.vector_storage import Qdrant
from db.mongo.mongodb import Mongodb

vectory = None
mongodb = None


def get_vectory():
    global vectory
    if vectory is None:
        print("callme")
        vectory = Qdrant().document_store
    return vectory


def get_mongodb():
    global mongodb
    if not mongodb:
        mongodb = Mongodb()
    return mongodb
