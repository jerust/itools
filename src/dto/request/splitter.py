from pydantic import BaseModel


class SplitterRequest(BaseModel):
    content: str
