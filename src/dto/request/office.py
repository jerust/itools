from pydantic import BaseModel


class DocxReaderRequest(BaseModel):
    filepath: str


class PdfReaderRequest(BaseModel):
    filepath: str


class ExcelReaderRequest(BaseModel):
    filepath: str
    readmode: str
    sheet: str
