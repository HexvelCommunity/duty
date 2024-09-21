from __future__ import annotations

import abc
import typing

from lib.hexable.base.wrapper import BaseWrapper

FieldsTypevar = typing.TypeVar("FieldsTypevar")


class ABCPage(BaseWrapper, abc.ABC):

    _mention_prefix: str

    @property
    @abc.abstractmethod
    def fullname(self) -> str: ...

    @property
    @abc.abstractmethod
    def id(self) -> int: ...

    def mention(self, alias: typing.Optional[str] = None) -> str:
        if alias:
            updated_alias = format(self, alias)
            mention = f"[{self._mention_prefix}{self.id}|{updated_alias}]"
        else:
            mention = f"[{self._mention_prefix}{self.id}|{self.fullname}]"
        return mention

    def _extra_fields_to_format(self) -> dict:
        return {"fullname": self.fullname, "id": self.id}

    def __format__(self, format_spec) -> str:
        format_value = super().__format__(format_spec)
        if format_spec.startswith("@"):
            format_value = format_value[1:]
            format_value = self.mention(format_value)
            return format_value
        return format_value

    def __repr__(self):
        return f"<hexlib.{self.__class__.__name__} fullname={self.fullname!r}>"


class User(ABCPage, typing.Generic[FieldsTypevar]):

    _mention_prefix = "id"
    default_fields = ("sex",)

    @property
    def fullname(self) -> str:
        return f"{self._rows['first_name']} {self._rows['last_name']}"

    @property
    def id(self) -> int:
        return self._rows["id"]

    @property
    def first_name(self) -> str:
        return self._rows["first_name"]

    @property
    def last_name(self) -> str:
        return self._rows["last_name"]
