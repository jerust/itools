from fastapi import APIRouter

from src.dto.request.embedding import EmbeddingRequest
from src.dto.response.embedding import EmbeddingRespond
from src.service import embedding as service

router = APIRouter()


@router.post(path="/itools/embedding")
async def embedding(body: EmbeddingRequest):
    return EmbeddingRespond(vector=service.embedding(body.content))
