import typing

from hexable.types.hexable_types.methods.base_category import BaseCategory
from hexable.types.hexable_types.responses.auth import *  # noqa: F401,F403  # type: ignore


class AuthCategory(BaseCategory):
    async def restore(
        self,
        last_name: str,
        phone: str,
        **kwargs: typing.Any,
    ) -> AuthRestoreResponseModel:
        """Method `auth.restore()`

        :param last_name: User last name.
        :param phone: User phone number.
        """

        params = self.get_set_params(locals())
        response = await self.api.method("auth.restore", params)
        model = AuthRestoreResponse
        return model(**response).response


__all__ = ("AuthCategory",)
