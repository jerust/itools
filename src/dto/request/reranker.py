from typing import List

from pydantic import BaseModel


class RerankerRequest(BaseModel):
    content: str
    rankers: List[str]
