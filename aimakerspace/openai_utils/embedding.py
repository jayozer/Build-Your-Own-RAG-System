from dotenv import load_dotenv
import openai
from typing import List
import os
import asyncio

#text-embedding-3-small	
#text-embedding-ada-002
class EmbeddingModel:
    def __init__(self, embeddings_model_name: str = "text-embedding-3-small"):
        load_dotenv()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

        if self.openai_api_key is None:
            raise ValueError(
                "OPENAI_API_KEY environment variable is not set. Please set it to your OpenAI API key."
            )
        openai.api_key = self.openai_api_key
        self.embeddings_model_name = embeddings_model_name

    async def async_get_embeddings(self, list_of_text: List[str]) -> List[List[float]]:
        return await openai.AsyncClient(api_key=self.openai_api_key).embeddings.create(
            input=list_of_text, model=self.embeddings_model_name
        )

    async def async_get_embedding(self, text: str) -> List[float]:
        return await openai.AsyncClient(api_key=self.openai_api_key).embeddings.create(
            input=text, model=self.embeddings_model_name
        )

    def get_embeddings(self, list_of_text: List[str]) -> List[List[float]]:
        return openai.Client(api_key=self.openai_api_key).embeddings.create(
            input=list_of_text, model=self.embeddings_model_name
        )

    def get_embedding(self, text: str) -> List[float]:
        return openai.Client(api_key=self.openai_api_key).embeddings.create(
            input=text, model=self.embeddings_model_name
        )


if __name__ == "__main__":
    embedding_model = EmbeddingModel()
    print(embedding_model.get_embedding("Hello, world!"))
    print(embedding_model.get_embeddings(["Hello, world!", "Goodbye, world!"]))
    print(asyncio.run(embedding_model.async_get_embedding("Hello, world!")))
    print(
        asyncio.run(
            embedding_model.async_get_embeddings(["Hello, world!", "Goodbye, world!"])
        )
    )
