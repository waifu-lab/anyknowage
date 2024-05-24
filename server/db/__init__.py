from db.vector.vector_storage import document_store
from db.mongo.mongodb import Mongodb

global vectory
vectory = document_store
global mongodb
mongodb = Mongodb()
