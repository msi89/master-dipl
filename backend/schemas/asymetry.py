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
