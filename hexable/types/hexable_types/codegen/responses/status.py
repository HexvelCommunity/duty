from hexable.types.hexable_types.base_model import Field
from hexable.types.hexable_types.objects import StatusStatus
from hexable.types.hexable_types.responses.base_response import BaseResponse


class StatusGetResponse(BaseResponse):
    response: "StatusStatus" = Field()
