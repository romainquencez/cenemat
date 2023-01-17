from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database.config import TORTOISE_ORM
from src.database.register import register_tortoise
from src.settings import FASTAPI_ALLOW_ORIGIN
from tortoise import Tortoise

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

# initialize FastAPI
app = FastAPI()

# CORS handle
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FASTAPI_ALLOW_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ORM handle
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def home():
    return "Hello, World!"


# only for testing
@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
