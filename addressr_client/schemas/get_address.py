from typing import Optional
from pydantic import BaseModel, Field


class CodeName(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None

class FlatType(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None


class Flat(BaseModel):
    number: Optional[int] = None
    type: Optional[FlatType] = None


class Number(BaseModel):
    number: Optional[int] = None


class Street(BaseModel):
    name: Optional[str] = None
    type: Optional[CodeName] = None


class LocalityClass(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None


class Locality(BaseModel):
    name: Optional[str] = None
    class_: Optional[LocalityClass] = Field(default=None, alias="class")


class State(BaseModel):
    abbreviation: Optional[str] = None
    name: Optional[str] = None


class Structured(BaseModel):
    confidence: Optional[int] = None
    flat: Optional[Flat] = None
    number: Optional[Number] = None
    street: Optional[Street] = None
    locality: Optional[Locality] = None
    postcode: Optional[str] = None
    state: Optional[State] = None

class AddressGetResponse(BaseModel):
    sla: Optional[str] = None
    structured: Optional[Structured] = None