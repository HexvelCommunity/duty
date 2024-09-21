import os

from fastapi import FastAPI
from loguru import logger

from app.config import settings
from app.repositories.iris import User
from lib.hexable.api import API, OwnerType

api: API | None = None
logger.disable("lib.hexable")


async def lifespan(app: FastAPI):
    global api
    logger.debug("App started")
    token = os.getenv("TOKEN")

    if token is None:
        logger.error("Token not found")
        raise Exception("Token not found") from ValueError("Token not found")

    user = User.get(id=715616525)

    if not user:
        user = User.create(
            id=settings.id,
            username=settings.username,
            prefix=settings.prefix,
            chats=settings.chats,
            secret=settings.secret,
        )

    api = API(token=token)
    api._owner_type = OwnerType.USER

    yield
    await api.close_session()
    logger.warning("App stopped")


async def get_api() -> API:
    if api is None:
        raise Exception("API instance is not initialized")
    return api


app = FastAPI(lifespan=lifespan)
