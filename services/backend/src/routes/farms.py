from auth.jwthandler import get_current_user
from crud.farms import get_farms_from_user
from fastapi import APIRouter, Depends, Request
from models.farms import Farm
from models.users import UserOut

router = APIRouter()


@router.get("/list", dependencies=[Depends(get_current_user)])
async def list_users(
    request: Request, current_user: UserOut = Depends(get_current_user)
) -> list[Farm]:
    async with request.app.state.db.acquire() as connection:
        async with connection.transaction():
            users = await get_farms_from_user(connection, current_user.id)
            return users
