from fastapi import APIRouter

from src.dto.request.converter import WordToPdfRequest
from src.dto.request.converter import PdfToHtmlRequest
from src.dto.response.converter import WordToPdfRespond
from src.dto.response.converter import PdfToHtmlRespond
from src.service import converter as service

router = APIRouter()


@router.post(path="/itools/converter/word-to-pdf")
async def word_to_pdf(body: WordToPdfRequest):
    return WordToPdfRespond(filepath=service.word_to_pdf(body.filepath))


@router.post(path="/itools/converter/pdf-to-html")
async def pdf_to_html(body: PdfToHtmlRequest):
    return PdfToHtmlRespond(filepath=service.pdf_to_html(body.filepath))
