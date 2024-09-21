from lib.json_parser import fields
from lib.json_parser.models import BaseModelMeta


class User(BaseModelMeta):
    id = fields.IntField()
    username = fields.StrField()
    prefix = fields.StrField()
    chats = fields.ListField(fields.JsonField())
    secret = fields.StrField()


class IrisRepository:
    def get_user(self, id: int) -> User | None:
        return User.get(id=id)

    def get_chats(self, id: int) -> list[dict]:
        user = User.get(id=id)
        return user.chats

    def create_user(self, user: User) -> User:
        user = User.create(
            id=user.id,
            username=user.username,
            prefix=user.prefix,
            chats=user.chats,
            secret=user.secret,
        )

        return user

    def update_user(self, user: User) -> User:
        user = User.update(
            id=user.id,
            username=user.username,
            prefix=user.prefix,
            chats=user.chats,
            secret=user.secret,
        )
