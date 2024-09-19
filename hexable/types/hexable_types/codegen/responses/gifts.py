import typing

from hexable.types.hexable_types.base_model import BaseModel, Field
from hexable.types.hexable_types.objects import GiftsGift
from hexable.types.hexable_types.responses.base_response import BaseResponse


class GiftsGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GiftsGift"] = Field()


class GiftsGetResponse(BaseResponse):
    response: "GiftsGetResponseModel" = Field()
