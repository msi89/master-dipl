from fastapi import UploadFile
import cv2
import uuid
import os

from libs.facedetect import asymetry_detection, getAsymetryMeasure
from schemas.asymetry import AsymmetryResult, FaceMeasure


class FaceSicknessService():

    async def detectMultiple(self, files: list[str]) -> list[AsymmetryResult]:
        results: list[AsymmetryResult] = []
        for file in files:
            data = await self.detectAsymmetry(file)
            results.append(data)
        return results

    async def detectAsymmetry(self, filename: str) -> AsymmetryResult:
        '''чтение изображения из временного файла и вызов функции 
        распознавания ориентиров лица'''
        file_path = os.path.abspath(filename)
        img = cv2.imread(file_path)

        data = AsymmetryResult(image_url=filename)

        report, face_count = asymetry_detection(img, file_path)
        data.result = report
        data.faces = face_count
        return data

    async def getFaceMeasure(self, file_path: str) -> list[FaceMeasure]:
        return getAsymetryMeasure(file_path)
