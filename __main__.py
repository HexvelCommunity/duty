from fastapi import FastAPI
from loguru import logger

from json_parser.fields import IntField, StrField
from json_parser.models import BaseModelMeta


class User(BaseModelMeta):
    id = IntField()
    username = StrField()
    token = StrField()


async def lifespan(app: FastAPI):
    logger.debug("Creating user...")
    user = User.get(id=2)
    if not user:
        user = User.create(id=2, username="user", token="12345")
    logger.debug("User got: {user}", user=user.to_dict())
    yield
    logger.warning("App stopped")


app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")
