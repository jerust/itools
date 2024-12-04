from fastapi import APIRouter, HTTPException

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
    content, error = service.docx_reader(body.filepath)
    if error:
        raise HTTPException(status_code=500)
    return DocxReaderRespond(content=content)


@router.post(path="/itools/office/pdf-reader")
async def pdf_reader(body: PdfReaderRequest):
    content, error = service.pdf_reader(body.filepath)
    if error:
        raise HTTPException(status_code=500)
    return PdfReaderRespond(content=content)


@router.post(path="/itools/office/excel-reader")
async def excel_reader(body: ExcelReaderRequest):
    content, error = service.excel_reader(body.filepath, body.readmode, body.sheet)
    if error:
        raise HTTPException(status_code=500)
    return ExcelReaderRespond(content=content)
