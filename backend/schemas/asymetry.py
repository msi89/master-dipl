from pydantic import BaseModel
from typing import Optional


class AsymmetryReport(BaseModel):
    symmetry: float
    status: Optional[str]
    descrition: Optional[str]


class AsymmetryResult(BaseModel):
    image_url: Optional[str]
    faces: Optional[int] = 0
    result: Optional[list[AsymmetryReport]] = []


class FaceMeasure(BaseModel):
    horizontal_asymmetry: Optional[float]
    vertical_asymmetry: Optional[float]
    proportionality: Optional[float]
    face_width: Optional[float]
    face_height: Optional[float]
    left_eye_width: Optional[float]
    right_eye_width: Optional[float]
    nose_width: Optional[float]
    mouth_width: Optional[float]
