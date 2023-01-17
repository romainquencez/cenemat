from src.settings import DATABASE_URL

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["src.database.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}
