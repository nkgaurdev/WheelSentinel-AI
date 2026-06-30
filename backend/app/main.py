from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.constants import API_PREFIX
from app.core.logging import logger
from app.database.init_db import create_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("===================================")
    logger.info("Starting WheelSentinel AI API")
    logger.info(f"Environment : {settings.ENVIRONMENT}")
    logger.info(f"Version     : {settings.APP_VERSION}")
    logger.info("===================================")
    
    create_database()
    logger.info("Database initialized successfully.")

    yield

    logger.info("Stopping WheelSentinel AI API")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Industrial AI Platform for Predictive Maintenance & Manufacturing Intelligence",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@app.get(f"{API_PREFIX}/health")
async def health():
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
    }