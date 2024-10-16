# models.py
from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class ImageDetection(Base):
    __tablename__ = 'image_detections'
    
    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String(255), nullable=False)
    name = Column(String(100))
    confidence = Column(Numeric(5, 3))
    x_min = Column(Numeric(10, 2))
    y_min = Column(Numeric(10, 2))
    x_max = Column(Numeric(10, 2))
    y_max = Column(Numeric(10, 2))
