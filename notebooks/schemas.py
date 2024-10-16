# schemas.py
from pydantic import BaseModel
from typing import Optional

class ImageDetectionBase(BaseModel):
    image_name: str
    name: Optional[str] = None
    confidence: Optional[float] = None
    x_min: Optional[float] = None
    y_min: Optional[float] = None
    x_max: Optional[float] = None
    y_max: Optional[float] = None

class ImageDetectionCreate(ImageDetectionBase):
    pass

class ImageDetection(ImageDetectionBase):
    id: int

    class Config:
        orm_mode = True
