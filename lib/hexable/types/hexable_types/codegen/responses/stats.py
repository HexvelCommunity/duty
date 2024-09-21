import typing

from lib.hexable.types.hexable_types.base_model import Field
from lib.hexable.types.hexable_types.objects import StatsPeriod, StatsWallpostStat
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class StatsGetPostReachResponse(BaseResponse):
    response: typing.List["StatsWallpostStat"] = Field()


class StatsGetResponse(BaseResponse):
    response: typing.List["StatsPeriod"] = Field()
