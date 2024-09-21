import typing

from lib.hexable.types.hexable_types.base_model import BaseModel, Field
from lib.hexable.types.hexable_types.objects import (
    AppsApp,
    GroupsGroup,
    NotificationsNotificationItem,
    NotificationsSendMessageItem,
    PhotosPhoto,
    UsersUser,
    VideoVideoFull,
)
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class NotificationsGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["NotificationsNotificationItem"] = Field()
    profiles: typing.Optional[typing.List["UsersUser"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroup"]] = Field(
        default=None,
    )
    last_viewed: typing.Optional[int] = Field(
        default=None,
    )
    photos: typing.Optional[typing.List["PhotosPhoto"]] = Field(
        default=None,
    )
    videos: typing.Optional[typing.List["VideoVideoFull"]] = Field(
        default=None,
    )
    apps: typing.Optional[typing.List["AppsApp"]] = Field(
        default=None,
    )
    next_from: typing.Optional[str] = Field(
        default=None,
    )
    ttl: typing.Optional[int] = Field(
        default=None,
    )


class NotificationsGetResponse(BaseResponse):
    response: "NotificationsGetResponseModel" = Field()


class NotificationsSendMessageResponse(BaseResponse):
    response: typing.List["NotificationsSendMessageItem"] = Field()
