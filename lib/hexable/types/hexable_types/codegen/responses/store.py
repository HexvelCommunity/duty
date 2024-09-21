import typing

from lib.hexable.types.hexable_types.base_model import BaseModel, Field
from lib.hexable.types.hexable_types.objects import (
    BaseStickerNew,
    StoreProduct,
    StoreStickersKeyword,
)
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class StoreGetFavoriteStickersResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["BaseStickerNew"] = Field()


class StoreGetFavoriteStickersResponse(BaseResponse):
    response: "StoreGetFavoriteStickersResponseModel" = Field()


class StoreGetProductsResponseModel(BaseModel):
    items: typing.List["StoreProduct"] = Field()
    count: int = Field()


class StoreGetProductsResponse(BaseResponse):
    response: "StoreGetProductsResponseModel" = Field()


class StoreGetStickersKeywordsResponseModel(BaseModel):
    count: int = Field()
    dictionary: typing.List["StoreStickersKeyword"] = Field()
    chunks_count: typing.Optional[int] = Field(
        default=None,
    )
    chunks_hash: typing.Optional[str] = Field(
        default=None,
    )


class StoreGetStickersKeywordsResponse(BaseResponse):
    response: "StoreGetStickersKeywordsResponseModel" = Field()


class StoreGetStickersKeywordsResponse(BaseResponse):
    response: "StoreGetStickersKeywordsResponseModel" = Field()
