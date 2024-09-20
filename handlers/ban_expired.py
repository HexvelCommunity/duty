from hexable.api import API
from hexable.exceptions import APIError
from hexable.types.hexable_types.codegen.objects import MessagesMessage
from models.iris import IrisDutyEvent, IrisDutyEventMethod
from utils import route


@route.method_handler(method=IrisDutyEventMethod.BAN_EXPIRED)
async def ban_expired(data: IrisDutyEvent, message: MessagesMessage, api: API):
    user = await api.users.get(user_ids=data.object.user_id, name_case="gen")

    message_id = await api.messages.send(
        peer_id=message.peer_id,
        message=f"🔥 Срок бана {user[0].first_name} {user[0].last_name} истёк.",
        random_id=0,
    )

    try:
        await api.messages.add_chat_user(
            chat_id=message.peer_id - 2000000000,
            user_id=user[0].id,
        )
    except APIError as e:
        if e.status_code == 15:
            await api.messages.edit(
                peer_id=message.peer_id,
                message_id=message_id,
                message=f"❗ Срок бана{user[0].first_name} {user[0].last_name} истёк. Нет привилегий для добавления в чат.",
            )
        else:
            await api.messages.edit(
                peer_id=message.peer_id,
                message_id=message_id,
                message=f"❗ Срок бана{user[0].first_name} {user[0].last_name} истёк. Не удалось добавить в чат.",
            )
    except Exception:
        await api.messages.edit(
            peer_id=message.peer_id,
            message_id=message_id,
            message=f"❗ Срок бана{user[0].first_name} {user[0].last_name} истёк. Не удалось добавить в чат. Неизвестная ошибка",
        )

    return {"response": "ok"}
