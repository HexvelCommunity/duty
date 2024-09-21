from fastapi import APIRouter, Depends

from app.config import settings
from app.core.utils import IrisHandlerManager
from app.depends import get_iris_service
from app.initialize import get_api
from app.schemas.iris.event import IrisDutyEvent
from app.schemas.iris.methods import IrisDutyEventMethod
from app.services.iris import IrisService
from lib.hexable.api import API

router = APIRouter()


@router.post("/callback")
async def callback(
    data: IrisDutyEvent,
    api: API = Depends(get_api),
    service: IrisService = Depends(get_iris_service),
):
    user = service.get_user(id=settings.id)

    if data.secret != user.secret:
        return {"response": "Неверный секретный код"}
    if data.user_id != user.id:
        return {"response": "Неверный идентификатор дежурного"}
    if data.method == IrisDutyEventMethod.PING:
        return {"response": "ok"}

    iris_handler_manager = IrisHandlerManager(service, data, api)
    iris_handler_manager.load_handlers()

    return await iris_handler_manager.dispatch_handler(settings.id)
