from loguru import logger

from hexable.api import API, register_handler
from models.event import Message


@register_handler(".с ку")
async def handle_greet(message: Message, api: API) -> None:
    user_id = message.from_id
    logger.info(f"Received greet command from {user_id}.")
