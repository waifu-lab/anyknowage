from haystack_integrations.document_stores.qdrant import QdrantDocumentStore

# https://haystack.deepset.ai/integrations/qdrant-document-store

document_store = QdrantDocumentStore(
    ":memory:",
    index="Document",
    embedding_dim=512,
    recreate_index=True,
    hnsw_config={"m": 16, "ef_construct": 64}
)