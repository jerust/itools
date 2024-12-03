from typing import List

from pydantic import BaseModel


class RerankerRespond(BaseModel):
    scores: List[float]
