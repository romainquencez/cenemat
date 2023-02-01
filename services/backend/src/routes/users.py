from datetime import timedelta

from auth.jwthandler import create_access_token, get_current_user
from auth.users import validate_user
from crud.users import create_user, get_user_from_id
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from models.users import UserIn, UserOut
from settings import settings

router = APIRouter()


@router.post("/login")
async def login(
    request: Request, user: OAuth2PasswordRequestForm = Depends()
) -> JSONResponse:
    # validate user
    user = await validate_user(request, user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # create access token
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=settings.jwt_access_token_expire_minutes),
    )

    # create response
    response = JSONResponse(
        content={"message": "You've successfully logged in. Welcome back!"}
    )

    # create cookie
    token = jsonable_encoder(access_token)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )

    return response


@router.post("/logout")
async def logout():
    # delete auth cookie and return response
    response = JSONResponse(content={"message": "You've successfully logged out."})
    response.delete_cookie(key="Authorization")
    return response


@router.post("/register", response_model=UserOut)
async def register_user(request: Request, user: UserIn) -> UserOut:
    async with request.app.state.db.acquire() as connection:
        # Open a transaction.
        async with connection.transaction():
            # create user
            user_id = await create_user(connection, user)
            # get user
            return await get_user_from_id(connection, user_id.id)


@router.get("/whoami", response_model=UserOut, dependencies=[Depends(get_current_user)])
async def read_users_me(current_user: UserOut = Depends(get_current_user)):
    return current_user
