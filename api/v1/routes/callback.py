from fastapi import APIRouter

router = APIRouter()


@router.post("/callback")
async def callback():
    pass
