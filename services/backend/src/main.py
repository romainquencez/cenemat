from pathlib import Path

import asyncpg
import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import farms, legal_status, users
from settings import settings

# initialize Sentry SDK before FastAPI
# see https://docs.sentry.io/platforms/python/guides/fastapi/
if settings.sentry_dsn:
    sentry_sdk.init(
        dsn=settings.sentry_dsn,
        traces_sample_rate=1.0,
    )

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
app.include_router(farms.router, prefix="/farms")
app.include_router(legal_status.router, prefix="/legal-status")
app.include_router(users.router, prefix="/users")

# add frontend staticfiles route
if Path("static/frontend").exists():
    app.mount(
        "/", StaticFiles(directory="static/frontend", html=True), name="static-frontend"
    )


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
