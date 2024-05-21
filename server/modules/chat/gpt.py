from haystack.components.builders.prompt_builder import PromptBuilder
from haystack_integrations.components.retrievers.qdrant import QdrantEmbeddingRetriever
from haystack import Pipeline
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.generators import OpenAIGenerator
from db import vectory
from models.ai_models import GPTModel
from models.basic_chat import BasicChat

prompt_template = """
Using only the information contained in these documents return a brief answer (max 50 words).
If the answer cannot be inferred from the documents, respond \"I don't know\".
Documents:
{% for doc in documents %}
    {{ doc.content }}
{% endfor %}
Question: {{question}}
Answer:
"""


class GPT(BasicChat):
    def __init__(self, model: GPTModel) -> None:
        llm = OpenAIGenerator(model=str(model))
        query_pipeline = Pipeline()
        query_pipeline.add_component(
            "text_embedder",
            SentenceTransformersTextEmbedder(
                model="BAAI/bge-small-en-v1.5",
                prefix="query:",
            ),
        )
        query_pipeline.add_component(
            "retriever", QdrantEmbeddingRetriever(document_store=vectory)
        )
        query_pipeline.add_component(
            "prompt_builder", PromptBuilder(template=prompt_template)
        )
        query_pipeline.add_component("generator", llm)
        query_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
        query_pipeline.connect("retriever.documents", "prompt_builder.documents")
        query_pipeline.connect("prompt_builder", "generator")
        self.query_pipeline = query_pipeline

    def ASK(self, question: str):
        results = self.query_pipeline.run(
            {
                "text_embedder": {"text": question},
                "prompt_builder": {"question": question},
            }
        )
        return results
