import typing

from lib.hexable.types.hexable_types.base_model import BaseModel, Field
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class TranslationsTranslateResponseModel(BaseModel):
    texts: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    source_lang: typing.Optional[str] = Field(
        default=None,
    )


class TranslationsTranslateResponse(BaseResponse):
    response: "TranslationsTranslateResponseModel" = Field()
