from pydantic import BaseModel


class WordToPdfRequest(BaseModel):
    filepath: str


class PdfToHtmlRequest(BaseModel):
    filepath: str
