from fastapi import APIRouter

from src.service import office as service
from src.dto.request.office import DocxReaderRequest
from src.dto.response.office import DocxReaderRespond
from src.dto.request.office import PdfReaderRequest
from src.dto.response.office import PdfReaderRespond
from src.dto.request.office import ExcelReaderRequest
from src.dto.response.office import ExcelReaderRespond

router = APIRouter()


@router.post(path="/itools/office/docx-reader")
async def docx_reader(body: DocxReaderRequest):
    return DocxReaderRespond(content=service.docx_reader(body.filepath))


@router.post(path="/itools/office/pdf-reader")
async def pdf_reader(body: PdfReaderRequest):
    return PdfReaderRespond(content=service.pdf_reader(body.filepath))


@router.post(path="/itools/office/excel-reader")
async def excel_reader(body: ExcelReaderRequest):
    return ExcelReaderRespond(
        content=service.excel_reader(body.filepath, body.readmode, body.sheet)
    )
