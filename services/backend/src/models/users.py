from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserIn(BaseModel):
    identifier: int
    email: str
    farm: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    membership_year: int
    password: str
    legal_status_id: UUID


class UserOut(BaseModel):
    id: UUID
    identifier: int
    email: str
    farm: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    membership_year: int
    created_at: datetime
    legal_status_id: UUID
    is_admin: bool
    is_deleted: bool


class UserPasswordOut(BaseModel):
    id: UUID
    password: str


class UserId(BaseModel):
    id: UUID
