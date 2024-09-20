import asyncio
import importlib
import os
from typing import Any, Dict, List, Optional

from loguru import logger

from hexable.api import API
from init import User
from models.iris import IrisDutyEvent


def load_handlers():
    """Автоматическая загрузка обработчиков."""
    handlers_dir = os.path.join(os.path.dirname(__file__), "../handlers")
    for filename in os.listdir(handlers_dir):
        if filename.endswith(".py"):
            module_name = f"handlers.{filename[:-3]}"
            importlib.import_module(module_name)


async def find_chat(data: IrisDutyEvent, api: API) -> Optional[Dict[str, Any]]:
    """Поиск чата по сообщению"""
    if not data:
        logger.warning("No message data provided for chat search.")
        return None

    user_id = data.user_id
    if user_id is None:
        logger.warning("No user_id provided in message data.")
        return None

    user = User.get(id=user_id)
    current_chats: List[Dict[str, Any]] = user.chats
    existing_chat = next(
        (chat for chat in current_chats if chat["id"] == data.object.chat), None
    )

    if existing_chat:
        if not data.message:
            history = await api.messages.get_history(peer_id=existing_chat["peer_id"])
            return history.items[0]
        else:
            chat = await api.messages.search(
                q=data.message.text if data.message else None,
                peer_id=existing_chat["peer_id"],
                count=1,
            )

        return chat.items[0]

    messages = await api.messages.search(q=data.message.text, count=5)
    chats = [chat for chat in messages.items if chat.peer_id > 2000000000]
    if not chats:
        logger.warning("No chats found with given message.")
        return None

    current_chats.append(
        {
            "id": data.object.chat,
            "peer_id": chats[0].peer_id,
            "installed": False,
        }
    )
    User.update(id=user_id, chats=current_chats)

    return chats[0]


async def get_all_history(api: API, peer_id: int, offset: int = 0):
    chat = await api.messages.get_history(count=1, peer_id=peer_id, offset=offset)
    count = chat.count

    while offset < count:
        try:
            chat = await api.messages.get_history(
                count=200, peer_id=peer_id, offset=offset
            )
        except Exception:
            await asyncio.sleep(3)
            continue

        offset += 200
        for item in chat.items:
            yield item
