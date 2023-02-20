from typing import List

from models.users import UserId, UserIn, UserOut, UserPasswordOut
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(connection, user: UserIn) -> UserId:
    user.password = password_context.hash(user.password)
    return UserId.parse_obj(
        await connection.fetchrow(
            """
                INSERT INTO public.user (
                    identifier,
                    email,
                    farm,
                    first_name,
                    last_name,
                    membership_year,
                    password,
                    legal_status_id
                ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
                RETURNING id
            """,
            *user.dict().values()
        )
    )


async def get_user_from_id(connection, user_id: int) -> UserOut:
    return UserOut.parse_obj(
        await connection.fetchrow(
            """
                SELECT
                    id,
                    identifier,
                    email,
                    farm,
                    first_name,
                    last_name,
                    membership_year,
                    created_at,
                    legal_status_id,
                    is_admin,
                    is_deleted
                FROM public.user WHERE id = $1 AND is_deleted IS FALSE
            """,
            user_id,
        )
    )


async def get_users(connection) -> List[UserOut]:
    records = await connection.fetch(
        """
            SELECT
                id,
                identifier,
                email,
                farm,
                first_name,
                last_name,
                membership_year,
                created_at,
                legal_status_id,
                is_admin,
                is_deleted
            FROM public.user ORDER BY identifier
        """,
    )
    return [UserOut.parse_obj(record) for record in records]


async def get_user_from_email(connection, email: str) -> UserOut:
    return UserOut.parse_obj(
        await connection.fetchrow(
            """
                SELECT
                    id,
                    identifier,
                    email,
                    farm,
                    first_name,
                    last_name,
                    membership_year,
                    created_at,
                    legal_status_id,
                    is_admin,
                    is_deleted
                FROM public.user WHERE email = $1 AND is_deleted IS FALSE
            """,
            email,
        )
    )


async def get_user_password(connection, email: str) -> UserPasswordOut | None:
    # try to get user's password with its email, or return None if email does not exist.
    record = await connection.fetchrow(
        "SELECT id, password FROM public.user WHERE email = $1 AND is_deleted IS FALSE",
        email,
    )
    return UserPasswordOut.parse_obj(record) if record else None
