import cv2
import os

from libs.facedetect import (
    asymetry_detection,
    getAsymetryMeasure,
    draw_grid_on_image,
    draw_grid_on_face
)
from schemas.asymetry import AsymmetryResult, FaceMeasure


class FaceSicknessService():

    async def detectMultiple(self, files: list[str]) -> list[AsymmetryResult]:
        results: list[AsymmetryResult] = []
        for file in files:
            data = await self.detectAsymmetry(file)
            results.append(data)
        return results

    async def detectAsymmetry(self,
                              filename: str,
                              measurable: bool = False,
                              grid=False) -> AsymmetryResult:
        '''чтение изображения из временного файла и вызов функции 
        распознавания ориентиров лица'''
        file_path = os.path.abspath(filename)
        img = cv2.imread(file_path)

        data = AsymmetryResult(image_url=filename)

        report, face_count = asymetry_detection(img, file_path)
        data.result = report
        data.faces = face_count
        if measurable:
            data.measure = getAsymetryMeasure(file_path)
        if grid:
            # draw_grid_on_image(file_path, True)
            draw_grid_on_face(file_path, True)
        return data

    async def getFaceMeasure(self, file_path: str) -> list[FaceMeasure]:
        return getAsymetryMeasure(file_path)
