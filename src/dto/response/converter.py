from pydantic import BaseModel


class WordToPdfRespond(BaseModel):
    filepath: str


class PdfToHtmlRespond(BaseModel):
    filepath: str
