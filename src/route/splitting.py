from fastapi import APIRouter

from src.dto.request.splitter import SplitterRequest
from src.dto.response.splitter import SplitterRespond
from src.service import splitting as service

router = APIRouter()


@router.post(path="/itools/splitting")
async def splitter(body: SplitterRequest):
    return SplitterRespond(slices=service.splitter(body.content))
