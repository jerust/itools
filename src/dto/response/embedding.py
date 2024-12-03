from typing import List

from pydantic import BaseModel


class EmbeddingRespond(BaseModel):
    vector: List[float]
