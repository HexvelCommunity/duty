from fastapi import APIRouter, Depends
from loguru import logger

from hexable.api import API
from init import get_api
from models.iris import IrisDutyEvent
from utils.helpers import find_chat

router = APIRouter()


@router.post("/callback")
async def callback(data: IrisDutyEvent, api: API = Depends(get_api)):
    logger.debug(data)
    chat = await find_chat(data, api)
    logger.debug(chat)
    return {"response": "ok"}
