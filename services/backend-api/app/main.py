from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .db import engine
from .entities import Base
from .routers import quotes


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="FertiFreight API", version="1.0.0", lifespan=lifespan)
app.include_router(quotes.router, prefix="/api/v1")


@app.get("/api/v1/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
