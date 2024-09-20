from loguru import logger

from config import id
from hexable.api import API
from hexable.types.hexable_types.codegen.objects import MessagesMessage
from init import User
from models.iris import IrisDutyEvent, IrisDutyEventMethod
from utils import route


@route.method_handler(method=IrisDutyEventMethod.SUBSCRIBE_SIGNALS)
async def subscribe_signals(data: IrisDutyEvent, message: MessagesMessage, api: API):
    user = User.get(id=id)
    chats = user.chats

    for chat in chats:
        if chat["id"] != data.object.chat:
            continue

        chat["installed"] = True
        logger.info(f"Чат с id '{data.object.chat}' найден и обновлен: {chat}")
        break

    User.update(id=id, chats=chats)

    edit_message = f"""
    🔥 Успешно. Я подписался на сигналы.
    🎊 Iris chat id: {data.object.chat}
    🗨️ Peer id: {message.peer_id}
    """

    await api.messages.edit(
        peer_id=message.peer_id,
        message_id=message.id,
        message=edit_message,
    )

    return {"response": "ok"}
