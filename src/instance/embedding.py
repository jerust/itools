from sentence_transformers import SentenceTransformer

from config import device, embedding

iembedding = SentenceTransformer(embedding, device=device)
