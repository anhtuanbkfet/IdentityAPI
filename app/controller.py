from fastapi import APIRouter

router = APIRouter()

@router.get("/check_exist")
async def check_exist(id=0):
    result = {"result": "OK"}
    return result