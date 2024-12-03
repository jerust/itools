from fastapi import APIRouter

from src.dto.request.reranker import RerankerRequest
from src.dto.response.reranker import RerankerRespond
from src.service import reranker as service

router = APIRouter()


@router.post(path="/itools/reranker")
async def reranker(body: RerankerRequest):
    return RerankerRespond(scores=service.reranker(body.content, body.rankers))
