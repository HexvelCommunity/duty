from datetime import datetime

from loguru import logger

from hexable.api import API
from hexable.exceptions import APIError
from hexable.types.hexable_types.codegen.objects import MessagesMessage
from models.iris import IrisDutyEvent, IrisDutyEventMethod
from utils import route
from utils.helpers import get_all_history


@route.method_handler(method=IrisDutyEventMethod.DELETE_MESSAGES_FROM_USER)
async def delete_message_from_user(
    data: IrisDutyEvent, message: MessagesMessage, api: API
):
    message_id = await api.messages.send(
        peer_id=message.peer_id,
        message=f"🔥 {message.from_id} удаление сообщеня от @id{data.object.user_id} из чата.",
        random_id=0,
    )

    cmids = []
    amount = data.object.amount

    async for message in get_all_history(api, message.peer_id):
        if datetime.now().timestamp() - message.date >= 86400:
            break

        if message.from_id == data.object.user_id and message.action is None:
            cmids.append(str(message.conversation_message_id))

    if amount and amount <= len(cmids):
        cmids = cmids[: len(cmids) - (len(cmids) - amount)]

    try:
        await api.messages.delete(
            peer_id=message.peer_id,
            cmids=cmids,
            delete_for_all=True,
            spam=True if data.object.is_spam else False,
        )

        await api.messages.edit(
            peer_id=message.peer_id,
            message_id=message_id,
            message=f"✅ @id{message.from_id} удаление сообщеня от @id{data.object.user_id} из чата. Сообщений удалено: {len(cmids)}.",
        )
    except APIError as e:
        await api.messages.edit(
            peer_id=message.peer_id,
            message_id=message_id,
            message=f"❗ @id{message.from_id} удаление сообщеня от @id{data.object.user_id} из чата. Ошибка: {e.description}",
        )
    except Exception:
        await api.messages.edit(
            peer_id=message.peer_id,
            message_id=message_id,
            message=f"❗ @id{message.from_id} удаление сообщеня от @id{data.object.user_id} из чата. Неизвестная ошибка.",
        )

    finally:
        return {"response": "ok"}
