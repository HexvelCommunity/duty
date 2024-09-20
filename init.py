import os

from dotenv import load_dotenv
from fastapi import FastAPI
from loguru import logger

from hexable.api import API, OwnerType
from json_parser import fields
from json_parser.models import BaseModelMeta

load_dotenv()


class User(BaseModelMeta):
    id = fields.IntField()
    username = fields.StrField()
    prefix = fields.StrField()
    chats = fields.ListField(fields.JsonField())
    secret = fields.StrField()
    installed = fields.BoolField()


api = None


def get_api() -> API:
    return api


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
            id=715616525,
            username="Hexik",
            prefix="id",
            chats=[],
            secret="secret",
            installed=True,
        )

    api = API(token=token)
    api._owner_type = OwnerType.USER

    yield
    await api.close_session()
    logger.warning("App stopped")


app = FastAPI(lifespan=lifespan)
