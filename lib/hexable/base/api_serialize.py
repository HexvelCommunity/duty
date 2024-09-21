import abc
import typing


class APISerializableMixin(abc.ABC):

    @abc.abstractmethod
    def represent_as_api_param(self) -> typing.Any: ...
