import dramatiq
from dramatiq.brokers.redis import RedisBroker
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
from modules.knowladge.knowledge import add_knowledge
from dotenv import load_dotenv
import os

load_dotenv()

redis_db = os.getenv("REDIS_DB", "127.0.0.1:6379")
redis_broker = RedisBroker(url=f"redis://{redis_db}/0")
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def ADD_knowledge(data: str | dict):
    add_knowledge(data)
