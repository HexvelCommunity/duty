import typing

from lib.hexable.types.hexable_types.base_model import BaseModel, Field
from lib.hexable.types.hexable_types.objects import PodcastExternalData
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class PodcastsSearchPodcastResponseModel(BaseModel):
    podcasts: typing.List["PodcastExternalData"] = Field()
    results_total: int = Field()


class PodcastsSearchPodcastResponse(BaseResponse):
    response: "PodcastsSearchPodcastResponseModel" = Field()
