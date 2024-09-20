from fastapi import APIRouter, Depends
from loguru import logger

from config import id
from hexable.api import API
from init import User, get_api
from models.iris import IrisDutyEvent, IrisDutyEventMethod
from utils import route
from utils.helpers import find_chat, load_handlers

router = APIRouter()


async def dispatch_handler(data: IrisDutyEvent, api: API):
    chat = await find_chat(data, api)
    if not chat:
        logger.warning("Chat not found, unable to proceed with handler.")
        return {"response": "Chat not found"}

    handler = route.get_handler(data.method)

    if handler:
        return await handler(data, chat, api)

    logger.info(f"No handler found for method: {data.method}")
    return {"response": "No handler matched"}


@router.post("/callback")
async def callback(data: IrisDutyEvent, api: API = Depends(get_api)):
    user = User.get(id=id)

    logger.debug(data)

    if data.secret != user.secret:
        return {"response": "Неверный секретный код"}
    if data.user_id != user.id:
        return {"response": "Неверный идентификатор дежурного"}
    if data.method == IrisDutyEventMethod.PING:
        return {"response": "ok"}

    return await dispatch_handler(data, api)


load_handlers()
