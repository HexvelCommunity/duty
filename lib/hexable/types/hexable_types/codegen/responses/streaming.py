import typing

from lib.hexable.types.hexable_types.base_model import BaseModel, Field
from lib.hexable.types.hexable_types.objects import StreamingStats
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class StreamingGetServerUrlResponseModel(BaseModel):
    endpoint: typing.Optional[str] = Field(
        default=None,
    )
    key: typing.Optional[str] = Field(
        default=None,
    )


class StreamingGetServerUrlResponse(BaseResponse):
    response: "StreamingGetServerUrlResponseModel" = Field()


class StreamingGetStatsResponse(BaseResponse):
    response: typing.List["StreamingStats"] = Field()


class StreamingGetStemResponseModel(BaseModel):
    stem: typing.Optional[str] = Field(
        default=None,
    )


class StreamingGetStemResponse(BaseResponse):
    response: "StreamingGetStemResponseModel" = Field()
