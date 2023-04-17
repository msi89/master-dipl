from fastapi import APIRouter, File, UploadFile, Request, Depends
from fastapi.responses import Response
from typing import Annotated
from services.detect import FaceSickness
from services.facesdetect import FaceSicknessService
from services.base import BaseService
from utils import medias


router = APIRouter()


@router.post("/clean")
async def clean_media_files(request: Request, service: BaseService = Depends()):
    service.cleanMediaFolder()
    return Response(status_code=204)


@router.post("/upload")
async def upload_file(request: Request, image: Annotated[UploadFile, File()],
                      service: FaceSickness = Depends()):
    url = medias.upload_file(image, "candidate")
    status = service.analyse_face(url)
    result = {}
    result["url"] = request.base_url._url + url
    result["status"] = status

    return result


@router.post("/detect")
async def detect_asymmetry(file: Annotated[
    UploadFile, File(...)
], service: FaceSicknessService = Depends()):
    result = await service.detectAsymmetry(file)
    return result


@router.post("/detect/multiple")
async def detect_asymmetry_multiple(files: Annotated[
    list[UploadFile], File(description="Multiple files as UploadFile")
], service: FaceSicknessService = Depends()):
    result = await service.detectMultiple(files)
    return result
