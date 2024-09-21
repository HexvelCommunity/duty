import json
import typing

from .base.json_parser import BaseJSONParser


class BuiltinJsonParser(BaseJSONParser):

    @staticmethod
    def dumps(data: typing.Dict[str, typing.Any]) -> typing.Union[str, bytes]:
        return json.dumps(data, ensure_ascii=False, separators=(",", ":"))

    @staticmethod
    def loads(string: typing.Union[str, bytes]) -> typing.Any:
        return json.loads(string)


json_parser_policy: typing.Type[BaseJSONParser]
json_parser_policy = BuiltinJsonParser
