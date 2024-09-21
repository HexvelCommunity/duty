import asyncio
import importlib
import os
from typing import Any, Dict, List, Optional

from loguru import logger

from app.core import route
from app.schemas.iris.event import IrisDutyEvent
from app.services.iris import IrisService
from lib.hexable.api import API


class IrisHandlerManager:
    def __init__(self, service: IrisService, data: IrisDutyEvent, api: API):
        self.service = service
        self.data = data
        self.api = api

    def load_handlers(self):
        handlers_dir = os.path.join("handlers")
        for filename in os.listdir(handlers_dir):
            if filename.endswith(".py"):
                module_name = f"handlers.{filename[:-3]}"
                importlib.import_module(module_name)

    async def search_peer_from_last_message(self) -> Optional[Dict[str, Any]]:
        if not self.data:
            logger.warning("No message data provided for chat search.")
            return None

        user_id = self.data.user_id
        if user_id is None:
            logger.warning("No user_id provided in message data.")
            return None

        user = self.service.get_user(id=user_id)
        current_chats: List[Dict[str, Any]] = user.chats

        existing_chat = next(
            (chat for chat in current_chats if chat["id"] == self.data.object.chat),
            None,
        )

        if existing_chat:
            if not self.data.message:
                history = await self.api.messages.get_history(
                    peer_id=existing_chat["peer_id"]
                )
                return history.items[0]
            else:
                chat = await self.api.messages.search(
                    q=self.data.message.text if self.data.message else None,
                    peer_id=existing_chat["peer_id"],
                    count=1,
                )
                return chat.items[0]

        messages = await self.api.messages.search(q=self.data.message.text, count=5)
        chats = [chat for chat in messages.items if chat.peer_id > 2000000000]
        if not chats:
            logger.warning("No chats found with the given message.")
            return None

        current_chats.append(
            {
                "id": self.data.object.chat,
                "peer_id": chats[0].peer_id,
                "installed": False,
            }
        )

        user.chats = current_chats
        self.service.update_user(user=user)

        return chats[0]

    async def get_all_history(self, peer_id: int, offset: int = 0):
        chat = await self.api.messages.get_history(
            count=1, peer_id=peer_id, offset=offset
        )
        count = chat.count

        while offset < count:
            try:
                chat = await self.api.messages.get_history(
                    count=200, peer_id=peer_id, offset=offset
                )
            except Exception as e:
                logger.error(f"Error fetching chat history: {e}")
                await asyncio.sleep(3)
                continue

            offset += 200
            for item in chat.items:
                yield item

    async def dispatch_handler(self, id: int):
        chat = await self.search_peer_from_last_message()

        if not chat:
            logger.warning("Chat not found, unable to proceed with handler.")
            return {"response": "Chat not found"}

        handler = route.get_handler(self.data.method)

        if handler:
            return await handler(self, self.data, chat, self.api, self.service)

        logger.info(f"No handler found for method: {self.data.method}")
        return {"response": "No handler matched"}
