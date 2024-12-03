from pydantic import BaseModel


class EmbeddingRequest(BaseModel):
    content: str
