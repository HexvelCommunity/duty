from hexable.types.hexable_types.base_model import BaseModel, Field
from hexable.types.hexable_types.responses.base_response import BaseResponse


class DownloadedGamesPaidStatusResponseModel(BaseModel):
    is_paid: bool = Field()


class DownloadedGamesPaidStatusResponse(BaseResponse):
    response: "DownloadedGamesPaidStatusResponseModel" = Field()
