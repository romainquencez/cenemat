from uuid import UUID

from pydantic import BaseModel


class LegalStatusIn(BaseModel):
    name: str


class LegalStatusOut(BaseModel):
    id: UUID
    name: str
