import enum
import typing

from lib.hexable.types.hexable_types.base_model import Field
from lib.hexable.types.hexable_types.objects import BaseUploadServer
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class BaseBoolResponse(BaseResponse):
    response: bool = Field()


class BaseGetUploadServerResponse(BaseResponse):
    response: "BaseUploadServer" = Field()


class BaseOkResponseModel(enum.IntEnum):
    OK = 1


class BaseOkResponse(BaseResponse):
    response: "BaseOkResponseModel" = Field(default=BaseOkResponseModel.OK)


class BaseUndefinedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
