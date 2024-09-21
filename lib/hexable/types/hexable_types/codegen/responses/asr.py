from lib.hexable.types.hexable_types.base_model import BaseModel, Field
from lib.hexable.types.hexable_types.objects import AsrTask
from lib.hexable.types.hexable_types.responses.base_response import BaseResponse


class AsrCheckStatusResponse(BaseResponse):
    response: "AsrTask" = Field()


class AsrProcessResponseModel(BaseModel):
    task_id: str = Field()


class AsrProcessResponse(BaseResponse):
    response: "AsrProcessResponseModel" = Field()
