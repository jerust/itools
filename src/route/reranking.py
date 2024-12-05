from fastapi import APIRouter

from src.dto.request.reranker import RerankerRequest
from src.dto.response.reranker import RerankerRespond
from src.service import reranking as service

router = APIRouter()


@router.post(path="/itools/reranking")
async def reranker(body: RerankerRequest):
    return RerankerRespond(scores=service.reranker(body.content, body.rankers))
