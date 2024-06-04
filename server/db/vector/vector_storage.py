from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
import os
# https://haystack.deepset.ai/integrations/qdrant-document-store

db_url = os.getenv("VECTOR_DB_URL", "localhost")
db_port = os.getenv("VECTOR_DB_PORT", "6333")


class Qdrant:
    def __init__(self):
        self.document_store = QdrantDocumentStore(
            db_url,
            port=db_port,
            index="Document",
            embedding_dim=1024,
            # recreate_index=True,
            hnsw_config={"m": 16, "ef_construct": 64},
        )
