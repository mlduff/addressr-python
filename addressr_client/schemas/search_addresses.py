from typing import Optional, List
from pydantic import BaseModel


class Highlight(BaseModel):
    sla: Optional[str] = None
    ssla: Optional[str] = None


class AddressSearchResult(BaseModel):
    sla: Optional[str] = None
    ssla: Optional[str] = None
    highlight: Optional[Highlight] = None
    score: Optional[float] = None
    pid: Optional[str] = None


AddressSearchResponse = List[AddressSearchResult]