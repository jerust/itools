from pydantic import BaseModel


class DocxReaderRespond(BaseModel):
    content: str


class PdfReaderRespond(BaseModel):
    content: str


class ExcelReaderRespond(BaseModel):
    content: str
