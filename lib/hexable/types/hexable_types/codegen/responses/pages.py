import typing

from lib.hexable.types.hexable_types.base_model import Field
from lib.hexable.types.hexable_types.objects import (
    PagesWikipage,
    PagesWikipageFull,
    PagesWikipageHistory,
)
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class PagesGetHistoryResponse(BaseResponse):
    response: typing.List["PagesWikipageHistory"] = Field()


class PagesGetTitlesResponse(BaseResponse):
    response: typing.List["PagesWikipage"] = Field()


class PagesGetVersionResponse(BaseResponse):
    response: "PagesWikipageFull" = Field()


class PagesGetResponse(BaseResponse):
    response: "PagesWikipageFull" = Field()


class PagesParseWikiResponse(BaseResponse):
    response: str = Field()


class PagesSaveAccessResponse(BaseResponse):
    response: int = Field()


class PagesSaveResponse(BaseResponse):
    response: int = Field()


class PagesSaveResponse(BaseResponse):
    response: int = Field()
