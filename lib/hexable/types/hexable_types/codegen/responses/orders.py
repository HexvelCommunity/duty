import typing

from lib.hexable.types.hexable_types.base_model import BaseModel, Field
from lib.hexable.types.hexable_types.objects import (
    OrdersAmount,
    OrdersOrder,
    OrdersSubscription,
)
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class OrdersChangeStateResponse(BaseResponse):
    response: str = Field()


class OrdersGetAmountResponse(BaseResponse):
    response: typing.List["OrdersAmount"] = Field()


class OrdersGetByIdResponse(BaseResponse):
    response: typing.List["OrdersOrder"] = Field()


class OrdersGetUserSubscriptionByIdResponse(BaseResponse):
    response: "OrdersSubscription" = Field()


class OrdersGetUserSubscriptionsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["OrdersSubscription"] = Field()


class OrdersGetUserSubscriptionsResponse(BaseResponse):
    response: "OrdersGetUserSubscriptionsResponseModel" = Field()


class OrdersGetResponse(BaseResponse):
    response: typing.List["OrdersOrder"] = Field()


class OrdersGetResponse(BaseResponse):
    response: typing.List["OrdersOrder"] = Field()
