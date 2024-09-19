from typing import Dict

from loguru import logger

from json_parser.base import BaseModel
from json_parser.fields import Field
from json_parser.storage import JsonStorage


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {name: attr for name, attr in attrs.items() if isinstance(attr, Field)}
        attrs['_meta'] = {
            'model_name': name.lower(),
            'fields': fields
        }
        return super().__new__(cls, name, bases, attrs)

class BaseModelMeta(BaseModel, metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field_name, field_instance in self._meta['fields'].items():
            setattr(self, field_name, kwargs.get(field_name))
        for field_name in self._meta['fields'].keys():
            if getattr(self, field_name, None) is None:
                logger.warning(f"Field '{field_name}' not set during initialization.")

    def to_dict(self) -> Dict:
        return {field_name: getattr(self, field_name) for field_name in self._meta['fields']}

    @classmethod
    def from_dict(cls, data: Dict) -> 'BaseModelMeta':
        return cls(**data)

    @classmethod
    def get(cls, id: int):
        data = JsonStorage.get(cls._meta['model_name'], id)
        if data:
            return cls.from_dict(data)
        return None

    @classmethod
    def save(cls, instance: 'BaseModelMeta'):
        if not hasattr(instance, 'id'):
            logger.error(f"Instance of '{cls.__name__}' has no attribute 'id'")
            raise AttributeError(f"Instance of '{cls.__name__}' has no attribute 'id'")
        JsonStorage.save(cls._meta['model_name'], getattr(instance, 'id'), instance.to_dict())

    @classmethod
    def delete(cls, id: int):
        JsonStorage.delete(cls._meta['model_name'], id)

    @classmethod
    def all(cls):
        return [cls.from_dict(item) for item in JsonStorage.all(cls._meta['model_name'])]

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        if 'id' not in kwargs:
            logger.error(f"Missing 'id' for instance creation in '{cls.__name__}'")
            raise ValueError("Field 'id' is required")
        cls.save(instance)
        return instance
