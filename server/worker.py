import dramatiq
from fastapi import UploadFile
from dramatiq.brokers.redis import RedisBroker
from modules.knowladge.knowledge import add_knowledge

redis_broker = RedisBroker(host="127.0.0.1", port=6739, db=0)
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def ADD_knowledge(data: str | UploadFile):
    add_knowledge(data)
