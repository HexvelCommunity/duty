import time

from pythonping import ping

from app.core import route
from lib.hexable.api import API
from lib.hexable.types.hexable_types.codegen.objects import MessagesMessage


@route.my_signal_handler(commands=["пинг"])
async def ping_handler(message: MessagesMessage, api: API):
    result = ping("api.vk.com", count=4)
    response_times = result.rtt_avg_ms if result.rtt_avg_ms else result.rtt_avg

    ping_time = time.time() - message.date

    await api.messages.edit(
        peer_id=message.peer_id,
        message_id=message.id,
        message=f"🏓 Задержка API VK: {response_times} мс.\n"
                f"🌐 Время пинга: {ping_time:.2f} сек.",
    )

    return {"response": "ok"}
