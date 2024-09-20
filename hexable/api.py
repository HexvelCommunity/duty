import asyncio
import enum
import re
import time
import typing

import aiohttp
from loguru import logger

from hexable.base.session_container import SessionContainerMixin
from hexable.exceptions import APIError
from hexable.types.hexable_types.base_model import BaseModel, Field


class APIResponse(BaseModel):
    response: typing.Optional[typing.Any] = Field(None)
    error: typing.Optional[str] = Field(None)


@enum.unique
class OwnerType(enum.Enum):
    USER = enum.auto()
    GROUP = enum.auto()
    NOBODY = enum.auto()


class API(SessionContainerMixin):
    def __init__(
        self,
        token: str,
        version: str = "5.199",
        api_url: str = "https://api.vk.com/method/",
        session: typing.Optional[aiohttp.ClientSession] = None,
    ) -> None:
        super().__init__(requests_session=session)
        self._token = token
        self._version = version
        self._api_url = api_url
        self._requests_delay = 1 / 20
        self._owner_type = OwnerType.NOBODY
        self._last_request_timestamp = 0.0
        self._stable_request_params = {"access_token": self._token, "v": self._version}

        self._update_requests_delay()

    @property
    def api_instance(self) -> typing.Self:
        return self

    def _update_requests_delay(self) -> None:
        self._requests_delay = 1 / 3 if self._owner_type == OwnerType.USER else 1 / 20

    async def method(self, method_name: str, request_params) -> typing.Any:
        method_name = re.sub(
            r"_(?P<let>[a-z])", lambda m: m.group("let").upper(), method_name
        )
        extra_request_params = {
            **self._stable_request_params,
            **request_params,
        }

        await asyncio.sleep(self._get_waiting_time())
        response = await self._make_api_request(method_name, extra_request_params)

        if "error" in response:
            await self.close_session()
            error = response["error"].copy()
            exception_class = APIError[error["error_code"]][0]
            raise exception_class(
                status_code=error.pop("error_code"),
                description=error.pop("error_msg"),
                request_params=error.pop("request_params"),
                extra_fields=error,
            )

        logger.debug("New response: {response}", response=response)
        return response

    async def _make_api_request(self, method: str, params: dict) -> typing.Any:
        while True:
            try:
                async with self.requests_session.post(
                    self._api_url + method, data=params
                ) as response:
                    parsed_response = await self.parse_json_body(response)
                    if parsed_response.get("error", {}).get("error_code") == 10:
                        logger.warning(
                            f"VK Internal server error while calling {method} ({params}). "
                            "Retrying in 10 seconds..."
                        )
                        await asyncio.sleep(10)
                    else:
                        return parsed_response
            except aiohttp.ClientResponseError as error:
                if error.status >= 500:
                    logger.warning(
                        f"Server error {error.status}. Retrying in 10 seconds..."
                    )
                    await asyncio.sleep(10)
                else:
                    raise error
            except aiohttp.ServerDisconnectedError:
                await self.refresh_session()

    def _get_waiting_time(self) -> float:
        now = time.time()
        wait_time = max(0, self._requests_delay - (now - self._last_request_timestamp))
        self._last_request_timestamp = now + wait_time
        return wait_time
