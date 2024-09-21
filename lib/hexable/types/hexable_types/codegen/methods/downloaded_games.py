import typing

from lib.hexable.types.hexable_types.methods.base_category import BaseCategory
from lib.hexable.types.hexable_types.responses.downloaded_games import *  # noqa: F401,F403  # type: ignore


class DownloadedGamesCategory(BaseCategory):
    async def get_paid_status(
        self,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> DownloadedGamesPaidStatusResponseModel:
        """Method `downloadedGames.getPaidStatus()`

        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.method("downloadedGames.getPaidStatus", params)
        model = DownloadedGamesPaidStatusResponse
        return model(**response).response


__all__ = ("DownloadedGamesCategory",)
