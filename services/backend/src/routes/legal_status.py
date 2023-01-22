from fastapi import APIRouter, Request
from models.legal_status import LegalStatusIn, LegalStatusOut

router = APIRouter()


@router.get("/")
async def get_legal_status(request: Request) -> list[LegalStatusOut]:
    async with request.app.state.db.acquire() as connection:
        records = await connection.fetch(
            "SELECT id, name FROM legal_status ORDER BY name"
        )
        return [LegalStatusOut.parse_obj(record) for record in records]


@router.post("/")
async def create_legal_status(
    request: Request, legal_status: LegalStatusIn
) -> LegalStatusOut:
    # get a connection from pool
    async with request.app.state.db.acquire() as connection:
        # open a transaction
        async with connection.transaction():

            # create legal status and get ID
            legal_status_db = await connection.fetchrow(
                "INSERT INTO legal_status VALUES (default, $1) RETURNING id",
                *legal_status.dict().values()
            )

            # get created legal status
            return LegalStatusOut.parse_obj(
                await connection.fetchrow(
                    "SELECT id, name FROM legal_status WHERE id = $1",
                    legal_status_db["id"],
                )
            )
