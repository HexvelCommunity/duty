import typing

from hexable.types.hexable_types.methods.base_category import BaseCategory
from hexable.types.hexable_types.objects import StreamingStats
from hexable.types.hexable_types.responses.streaming import *  # noqa: F401,F403  # type: ignore


class StreamingCategory(BaseCategory):
    async def get_server_url(
        self,
        **kwargs: typing.Any,
    ) -> StreamingGetServerUrlResponseModel:
        """Method `streaming.getServerUrl()`"""

        params = self.get_set_params(locals())
        response = await self.api.method("streaming.getServerUrl", params)
        model = StreamingGetServerUrlResponse
        return model(**response).response

    async def get_stats(
        self,
        end_time: typing.Optional[int] = None,
        interval: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.List[StreamingStats]:
        """Method `streaming.getStats()`

        :param end_time:
        :param interval:
        :param start_time:
        :param type:
        """

        params = self.get_set_params(locals())
        response = await self.api.method("streaming.getStats", params)
        model = StreamingGetStatsResponse
        return model(**response).response

    async def get_stem(
        self,
        word: str,
        **kwargs: typing.Any,
    ) -> StreamingGetStemResponseModel:
        """Method `streaming.getStem()`

        :param word:
        """

        params = self.get_set_params(locals())
        response = await self.api.method("streaming.getStem", params)
        model = StreamingGetStemResponse
        return model(**response).response


__all__ = ("StreamingCategory",)
