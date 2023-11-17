from fastapi import APIRouter

router = APIRouter()
"""
Check the Id of an identity is valid or not (Valid if this Id is existed on FIS database)
"""
@router.get("/check-valid")
async def check_valid(id=0):
    ret = True if int(id) % 2 == 0 else False 

    identity ={
            "id": id,
            "username": "admin",
            "roles": ["admin"],
            "token": None,
        }
    if ret:
        return {
        "success": ret,
        "message": "Identity is valid and can be used",
        "result": identity,
        }
    else:
        return {
            "success": ret,
            "code": -1,
            "message": "Identity is not found",
        }