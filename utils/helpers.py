from typing import Any, Dict, Optional

from loguru import logger

from hexable.api import API
from json_parser import fields
from json_parser.models import BaseModelMeta
from models.iris import IrisDutyEvent


class User(BaseModelMeta):
    id = fields.IntField()
    username = fields.StrField()
    prefix = fields.StrField()
    chats = fields.ListField(fields.JsonField())
    secret = fields.StrField()
    installed = fields.BoolField()


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
    current_chats = user.to_dict().get("chats", [])
    existing_chat = next(
        (chat for chat in current_chats if chat["id"] == data.object.chat), None
    )

    if existing_chat:
        return existing_chat

    messages = await api.messages.search(q=data.message.text, count=5)
    chats = [chat for chat in messages.items if chat.peer_id > 2000000000]
    if not chats:
        logger.warning("No chats found with given message.")
        return None

    current_chats.append(
        {
            "id": data.object.chat,
            "iris_id": data.object.user_id,
            "peer_id": chats[0].peer_id,
            "installed": False,
        }
    )

    User.update(id=user_id, chats=current_chats)
    return chats[0]
