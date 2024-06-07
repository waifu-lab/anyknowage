from db import get_vectory
from haystack import Pipeline
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack.components.generators import OpenAIGenerator
from haystack.components.readers import ExtractiveReader
from haystack_integrations.components.embedders.fastembed import FastembedTextEmbedder
from haystack_integrations.components.retrievers.qdrant import QdrantEmbeddingRetriever
from haystack.utils import Secret
from models.ai_models import GPTModel
from models.basic_chat import BasicChat

prompt_template = """
First Using only the information contained in these documents return a brief answer (max {{max_tokens}} words).
If the answer cannot be inferred from the documents, find the answer from your external knowledge, and tell user \"Source Not From Knowledge\".
Documents:
{% for doc in documents %}
    {{ doc.content }}
{% endfor %}
Question: {{question}}
Answer:
"""


class GPT(BasicChat):
    def __init__(self, model: GPTModel, maxtoken: int, key: str) -> None:
        self.maxtoken = maxtoken
        if get_vectory().count_documents() == 0:
            raise Exception("No documents in the database")
        llm = OpenAIGenerator(
            model=str(model),
            api_key=Secret.from_token(key),
            generation_kwargs={"max_tokens": maxtoken},
        )
        reader = ExtractiveReader()
        reader.warm_up()
        query_pipeline = Pipeline()
        query_pipeline.add_component(
            "text_embedder",
            FastembedTextEmbedder(
                model="intfloat/multilingual-e5-large", parallel=0, prefix="query:"
            ),
        )
        query_pipeline.add_component(
            "retriever", QdrantEmbeddingRetriever(document_store=get_vectory(), top_k=2)
        )
        query_pipeline.add_component(
            "prompt_builder", PromptBuilder(template=prompt_template)
        )
        query_pipeline.add_component("generator", llm)
        query_pipeline.add_component(instance=reader, name="reader")
        query_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
        query_pipeline.connect("retriever.documents", "prompt_builder.documents")
        query_pipeline.connect("retriever.documents", "reader.documents")
        query_pipeline.connect("prompt_builder", "generator")
        self.query_pipeline = query_pipeline

    def ASK(self, question: str):
        results = self.query_pipeline.run(
            {
                "text_embedder": {"text": question},
                "prompt_builder": {"question": question, "max_tokens": self.maxtoken},
                "reader": {"query": question, "top_k": 2},
            },
            include_outputs_from=["reader"],
        )
        return results
