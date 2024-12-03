from typing import List

from pydantic import BaseModel


class SplitterRespond(BaseModel):
    slices: List[str]
