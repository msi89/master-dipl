from fastapi import APIRouter, File, UploadFile, Request, Depends, Form, HTTPException
from fastapi.responses import Response
from typing import Annotated
# from services.detect import FaceSickness
from services.facesdetect import FaceSicknessService
from services.base import BaseService
from utils import medias
import uuid
import os

router = APIRouter()


@router.post("/clean")
async def clean_media_files(request: Request, service: BaseService = Depends()):
    service.cleanMediaFolder()
    return Response(status_code=204)


# @router.post("/upload")
# async def upload_file(request: Request, image: Annotated[UploadFile, File()],
#                       service: FaceSickness = Depends()):
#     url = medias.upload_file(image, "candidate")
#     status = service.analyse_face(url)
#     result = {}
#     result["url"] = request.base_url._url + url
#     result["status"] = status

#     return result


@router.post("/asymmetry")
async def detect_asymmetry(file: Annotated[
    UploadFile, File(...)
], service: FaceSicknessService = Depends()):
    filename = f"media/{uuid.uuid1()}.jpg"
    file_path = os.path.abspath(filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    result = await service.detectAsymmetry(
        filename=filename,
        measurable=True,
        grid=True
    )
    return result


@router.post("/asymmetry/multiple")
async def detect_asymmetry_multiple(files: Annotated[
    list[UploadFile], File(description="Multiple files as UploadFile")
], service: FaceSicknessService = Depends()):
    fielpaths = []
    for file in files:
        filename = f"media/{uuid.uuid1()}.jpg"
        file_path = os.path.abspath(filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
            fielpaths.append(filename)
    result = await service.detectMultiple(fielpaths)
    return result


@router.post("/asymmetry/measures")
async def get_asymmetry_measures(file_path: Annotated[str, Form()],
                                 service: FaceSicknessService = Depends()):
    absfile = os.path.abspath(file_path)
    if not os.path.exists(absfile):
        raise HTTPException(400, "image path does not exists")
    result = await service.getFaceMeasure(absfile)
    return result
