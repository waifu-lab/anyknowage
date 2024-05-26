import dramatiq
from models.tempfile import Temp_File
from dramatiq.brokers.redis import RedisBroker
from modules.knowladge.knowledge import add_knowledge
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore

redis_broker = RedisBroker(url="redis://127.0.0.1:6379/0")
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def ADD_knowledge(data: str | Temp_File):
    add_knowledge(data)
