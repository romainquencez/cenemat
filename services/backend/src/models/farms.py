from uuid import UUID

from pydantic import BaseModel


class Farm(BaseModel):
    id: UUID
    legal_status_name: str
    name: str
