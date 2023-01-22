import asyncpg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import legal_status, users
from settings import settings

# initialize FastAPI
app = FastAPI()

# CORS handle
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.fastapi_allow_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# add routes
app.include_router(legal_status.router, prefix="/legal-status")
app.include_router(users.router, prefix="/users")


# initialize db's pool on startup
@app.on_event("startup")
async def startup():
    app.state.db = await asyncpg.create_pool(
        host=settings.postgres_host,
        port=settings.postgres_port,
        user=settings.postgres_user,
        database=settings.postgres_db,
        password=settings.postgres_password,
    )
