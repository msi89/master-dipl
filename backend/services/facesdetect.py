from fastapi import UploadFile
import cv2
import uuid
import os

from libs.asymmetry import asymetry_detection
from schemas.asymetry import AsymmetryResult


class FaceSicknessService():

    async def detectMultiple(self, files: list[UploadFile]) -> list[AsymmetryResult]:
        results: list[AsymmetryResult] = []
        for file in files:
            data = await self.detectAsymmetry(file)
            results.append(data)
        return results

    async def detectAsymmetry(self, file: UploadFile) -> AsymmetryResult:
        filename = f"media/{uuid.uuid1()}.jpg"
        file_path = os.path.abspath(filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        '''чтение изображения из временного файла и вызов функции 
        распознавания ориентиров лица'''
        img = cv2.imread(file_path)

        data = AsymmetryResult(image_url=filename)

        report, face_count = asymetry_detection(img, file_path)
        data.result = report
        data.faces = face_count
        return data
