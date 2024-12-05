from typing import List

from src.instance.reranker import ireranker


def reranker(content: str, rankers: List[str]) -> List[float]:
    sentences = [[content, ranker] for ranker in rankers]
    return ireranker.predict(sentences)
