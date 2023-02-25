from typing import List

from models.farms import Farm


async def get_farms_from_user(connection, user_id: int) -> List[Farm]:
    records = await connection.fetch(
        """
            SELECT f.id, ls.name AS legal_status_name, f.name
            FROM public.farm f
            INNER JOIN legal_status ls ON f.legal_status_id = ls.id
            INNER JOIN user_farm uf on f.id = uf.farm_id
            WHERE uf.user_id = $1
        """,
        user_id,
    )
    return [Farm.parse_obj(record) for record in records]
