from sentence_transformers import CrossEncoder

from config import reranker

ireranker = CrossEncoder(reranker)
