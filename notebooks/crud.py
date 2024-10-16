# crud.py
from sqlalchemy.orm import Session
from models import ImageDetection
from schemas import ImageDetectionCreate

def create_image_detection(db: Session, detection: ImageDetectionCreate):
    db_detection = ImageDetection(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection

def get_image_detection(db: Session, detection_id: int):
    return db.query(ImageDetection).filter(ImageDetection.id == detection_id).first()

def get_image_detections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ImageDetection).offset(skip).limit(limit).all()

def update_image_detection(db: Session, detection_id: int, detection: ImageDetectionCreate):
    db_detection = db.query(ImageDetection).filter(ImageDetection.id == detection_id).first()
    if db_detection:
        for key, value in detection.dict().items():
            setattr(db_detection, key, value)
        db.commit()
        db.refresh(db_detection)
    return db_detection

def delete_image_detection(db: Session, detection_id: int):
    db_detection = db.query(ImageDetection).filter(ImageDetection.id == detection_id).first()
    if db_detection:
        db.delete(db_detection)
        db.commit()
    return db_detection
