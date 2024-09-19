import typing

from hexable.types.hexable_types.base_model import BaseModel, Field
from hexable.types.hexable_types.responses.base_response import BaseResponse


class AuthRestoreResponseModel(BaseModel):
    success: typing.Optional[int] = Field(
        default=None,
    )
    sid: typing.Optional[str] = Field(
        default=None,
    )


class AuthRestoreResponse(BaseResponse):
    response: "AuthRestoreResponseModel" = Field()
