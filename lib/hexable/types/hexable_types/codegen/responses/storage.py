import typing

from lib.hexable.types.hexable_types.base_model import Field
from lib.hexable.types.hexable_types.objects import StorageValue
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class StorageGetKeysResponse(BaseResponse):
    response: typing.List[str] = Field()


class StorageGetResponse(BaseResponse):
    response: typing.List["StorageValue"] = Field()
