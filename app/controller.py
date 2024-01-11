from fastapi import APIRouter, File, UploadFile, Request
from typing import Any, List
from typing_extensions import Annotated
import os


router = APIRouter()

UPLOADED_FOLDER = "uploaded_files"


def save_file(saved_dir, file_data, filename):
    if not os.path.isdir(saved_dir):
        os.mkdir(saved_dir)
    file_path = os.path.join(saved_dir, filename.replace(" ", "-"))
    with open(file_path,'wb+') as f:
        f.write(file_data)
        f.close()
    return filename


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

from time import time
@router.post("/file/")
async def create_file(file: Annotated[bytes, File()]):
    saved_dir = os.path.join(os.getcwd(), UPLOADED_FOLDER)
    filename = "{}".format(time())
    file_name = save_file(saved_dir, file, filename)
    return {
        "success": True,
        "file": file_name,
        "file_size": len(file),
        }


@router.post("/uploadfile/")
async def create_upload_file(image: UploadFile=File(...)):
    """
Uppload single image file into server.
    """
    saved_dir = os.path.join(os.getcwd(), UPLOADED_FOLDER)

    file_name = save_file(saved_dir, image.file.read(), image.filename)

    return {
        "success": True,
        "file": file_name,
        "file_size": len(image.file.read())
        }


@router.post("/uploadfiles/")
async def create_upload_files(images: List[UploadFile]=File(...)):
    """
Uppload image files into server.
    """
    saved_dir = os.path.join(os.getcwd(), UPLOADED_FOLDER)
    saved_files = []
    
    for image in images:
        saved_files.append(save_file(saved_dir, image.file.read(), image.filename))
    return {
        "success": True,
        "files": saved_files,
        }


