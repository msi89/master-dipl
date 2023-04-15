from fastapi import APIRouter, File, UploadFile, Request
from typing import Annotated
from views import detect, test
from utils import medias

router = APIRouter()


@router.get("/test")
def page():
    return {"request": test.cwd()}


@router.post("/upload")
async def upload_file(request: Request, image: Annotated[UploadFile, File()]):
    url = medias.upload_file(image, "candidate")
    status = detect.analyse_face(url)
    result = {}
    result["url"] = request.base_url._url + url
    result["status"] = status

    return result
