from crud.users import get_user_from_id, get_user_password
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from models.users import UserOut
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def validate_user(
    request: Request, user: OAuth2PasswordRequestForm = Depends()
) -> UserOut:
    async with request.app.state.db.acquire() as connection:
        async with connection.transaction():
            # get user from DB
            db_user = await get_user_password(connection, user.username)

            # validate user
            if db_user is None or not password_context.verify(
                user.password, db_user.password
            ):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                )

        return await get_user_from_id(connection, db_user.id)
