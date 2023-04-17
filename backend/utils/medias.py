from fastapi import UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from typing import List
import shutil
import os
import uuid

base_dir = os.path.join(os.getcwd(), "media")

if not os.path.exists(base_dir):
    os.makedirs(base_dir)


def upload_file(media: UploadFile = File(...), dest: str = None) -> str:
    path = f'{base_dir}' if dest is None else f'{base_dir}/{dest}'
    os.makedirs(name=path, exist_ok=True)
    path = normalize_file_path(os.path.join(path, media.filename))

    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(media.file, buffer)
    output = get_file_name(path)
    output = os.path.join("media", output) if dest is None else os.path.join(
        "media", dest, output)
    return output


def upload_multiple_files(files: List[UploadFile] = File(...),
                          dest: str = None):
    for f in files:
        upload_file(f, dest=dest)


async def get_media(filename: str) -> FileResponse:
    return FileResponse(get_media_path(filename))


async def get_media_path(filename: str) -> str:
    path = f'{base_dir}/{filename}'
    if os.path.exists(path):
        return path
    raise HTTPException(404, detail='File does not exist!')


def get_file_name(filepath: str) -> str:
    return filepath.split("/")[-1]


def get_file_ext(filepath: str) -> str:
    return get_file_name(filepath).split(".")[-1]


def normalize_file_path(path: str) -> str:
    if os.path.exists(path):
        s = str(uuid.uuid4()).split("-")[0]
        name, ext = os.path.splitext(path)
        return normalize_file_path(f"{name}_{s}{ext}")
    return path
