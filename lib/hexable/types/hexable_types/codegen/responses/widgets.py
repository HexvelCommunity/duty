import typing

from lib.hexable.types.hexable_types.base_model import BaseModel, Field
from lib.hexable.types.hexable_types.objects import (
    WidgetsWidgetComment,
    WidgetsWidgetPage,
)
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class WidgetsGetCommentsResponseModel(BaseModel):
    count: int = Field()
    posts: typing.List["WidgetsWidgetComment"] = Field()


class WidgetsGetCommentsResponse(BaseResponse):
    response: "WidgetsGetCommentsResponseModel" = Field()


class WidgetsGetPagesResponseModel(BaseModel):
    count: int = Field()
    pages: typing.List["WidgetsWidgetPage"] = Field()


class WidgetsGetPagesResponse(BaseResponse):
    response: "WidgetsGetPagesResponseModel" = Field()
