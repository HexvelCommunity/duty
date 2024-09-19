import typing


class BaseWrapper:
    def __init__(self, rows: dict) -> None:
        self._rows = rows

    @property
    def rows(self) -> dict:
        return self._rows

    def __getitem__(self, item: str) -> typing.Any:
        return self._rows[item]

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f"{cls_name}({self._rows})"
