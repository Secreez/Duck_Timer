from fastapi import APIRouter

router = APIRouter()

@router.get("/timer")
async def read_timer():
    return {"message": "Timer endpoint"}