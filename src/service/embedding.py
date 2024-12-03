from typing import List

from src.instance.embedding import iembedding


def embedding(content: str) -> List[float]:
    return iembedding.encode(content, normalize_embeddings=True)
