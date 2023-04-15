import os
import shutil
from fastapi import UploadFile


def cwd():
    return {
        "cwd": os.getcwd(),
    }


def upload(image: UploadFile) -> str:
    img_path = os.path.join(os.getcwd(), "media", image.filename)
    with open(img_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return img_path
