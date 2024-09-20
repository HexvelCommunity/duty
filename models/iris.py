import enum
from datetime import datetime
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T", bound="BaseModel")


class IrisDutyEventMethod(enum.Enum):
    """Спасибо Юре за предоставление моделей (я бы заебался это всё писать)"""

    ADD_USER = "addUser"
    BAN_EXPIRED = "banExpired"
    BAN_GET_REASON = "banGetReason"
    BIND_CHAT = "bindChat"
    DELETE_MESSAGES_FROM_USER = "deleteMessagesFromUser"
    DELETE_MESSAGES = "deleteMessages"
    FORBIDDEN_LINKS = "forbiddenLinks"
    PING = "ping"
    PRINT_BOOKMARK = "printBookmark"
    SUBSCRIBE_SIGNALS = "subscribeSignals"
    TO_GROUP = "toGroup"
    SEND_SIGNAL = "sendSignal"
    SEND_MY_SIGNAL = "sendMySignal"
    HIRE_API = "hireApi"
    MEET_CHAT_DUTY = "meetChatDuty"
    MESSAGES_DELETE_BY_TYPE = "messages.deleteByType"
    GROUP_BOTS_INVITED = "groupbots.invited"
    MESSAGES_RECOGNISE_AUDIO_MESSAGE = "messages.recogniseAudioMessage"


class IrisDutyEventMessage(BaseModel):
    conversation_message_id: int
    from_id: int
    date: datetime
    text: str


class IrisDutyEventObject(BaseModel):
    from_id: int | None = Field(default=None)
    chat: str | None = Field(default=None)
    text: str | None = Field(default=None)
    conversation_message_id: int | None = Field(default=None)
    is_spam: bool | None = Field(default=None)
    silent: bool | None = Field(default=None)
    user_id: int | None = Field(default=None)
    member_ids: list[int] | None = Field(default=None)
    reason: str | None = Field(default=None)
    source: str | None = Field(default=None)
    amount: int | None = Field(default=None)
    local_id: int | None = Field(default=None)
    local_ids: list[int] | None = Field(default=None)
    description: str | None = Field(default=None)
    value: str | None = Field(default=None)
    price: int | None = Field(default=None)
    group_id: int | None = Field(default=None)


class IrisDutyEvent(BaseModel, Generic[T]):
    user_id: int
    method: IrisDutyEventMethod
    secret: str
    message: IrisDutyEventMessage | None
    object: IrisDutyEventObject | T | None
