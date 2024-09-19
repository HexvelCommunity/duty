import typing

from hexable.types.hexable_types.base_model import Field
from hexable.types.hexable_types.objects import (SecureGiveEventStickerItem,
                                                 SecureLevel,
                                                 SecureSetCounterItem,
                                                 SecureSmsNotification,
                                                 SecureTokenChecked,
                                                 SecureTransaction)
from hexable.types.hexable_types.responses.base_response import BaseResponse


class SecureCheckTokenResponse(BaseResponse):
    response: "SecureTokenChecked" = Field()


class SecureGetAppBalanceResponse(BaseResponse):
    response: int = Field()


class SecureGetSMSHistoryResponse(BaseResponse):
    response: typing.List["SecureSmsNotification"] = Field()


class SecureGetTransactionsHistoryResponse(BaseResponse):
    response: typing.List["SecureTransaction"] = Field()


class SecureGetUserLevelResponse(BaseResponse):
    response: typing.List["SecureLevel"] = Field()


class SecureGiveEventStickerResponse(BaseResponse):
    response: typing.List["SecureGiveEventStickerItem"] = Field()


class SecureSendNotificationResponse(BaseResponse):
    response: typing.List[int] = Field()


class SecureSetCounterArrayResponse(BaseResponse):
    response: typing.List["SecureSetCounterItem"] = Field()
