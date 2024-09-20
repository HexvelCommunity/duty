import time

from hexable.api import API
from hexable.types.hexable_types.codegen.objects import MessagesMessage
from models.iris import IrisDutyEvent
from utils import route


@route.message_handler(commands=[".с пинг"])
async def get_ping(data: IrisDutyEvent, message: MessagesMessage, api: API):
    ping = time.time() - message.date

    await api.messages.edit(
        peer_id=message.peer_id,
        message_id=message.id,
        message=f"🌐 PingTime: {ping:.2f}s",
    )

    return {"response": "ok"}
