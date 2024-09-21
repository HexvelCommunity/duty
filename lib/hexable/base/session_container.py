from __future__ import annotations

import abc
import contextlib
import ssl
import typing

import aiohttp

from lib.hexable.json_parsers import BaseJSONParser, json_parser_policy
from lib.hexable.types.hexable_types.categories import APICategories


class SessionContainerMixin(APICategories, abc.ABC):
    def __init__(
        self,
        *,
        requests_session: typing.Optional[aiohttp.ClientSession] = None,
        json_parser: typing.Optional[BaseJSONParser] = None,
    ) -> None:
        self.__session = requests_session
        self.__json_parser = json_parser or json_parser_policy

    @property
    def requests_session(self) -> aiohttp.ClientSession:
        if self.__session is None or self.__session.closed:
            self.__session = self._init_aiohttp_session()

        return self.__session

    async def __aenter__(self) -> SessionContainerMixin:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close_session()

    async def close_session(self) -> None:
        if self.__session is not None:
            await self.__session.close()

    async def parse_json_body(self, response: aiohttp.ClientResponse, **kwargs) -> dict:
        return await response.json(loads=self.__json_parser.loads, **kwargs)

    def _init_aiohttp_session(self) -> aiohttp.ClientSession:
        return aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=ssl.SSLContext()),
            skip_auto_headers={"User-Agent"},
            raise_for_status=True,
            json_serialize=self.__json_parser.dumps,
        )

    async def refresh_session(self) -> None:
        if not self.__session.closed:
            with contextlib.suppress(Exception):
                await self.__session.close()
        self.__session = self._init_aiohttp_session()
