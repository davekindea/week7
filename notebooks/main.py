# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, Base, get_db

# Create the tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/image_detections/", response_model=schemas.ImageDetection)
def create_detection(detection: schemas.ImageDetectionCreate, db: Session = Depends(get_db)):
    return crud.create_image_detection(db=db, detection=detection)

@app.get("/image_detections/{detection_id}", response_model=schemas.ImageDetection)
def read_detection(detection_id: int, db: Session = Depends(get_db)):
    db_detection = crud.get_image_detection(db, detection_id=detection_id)
    if db_detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return db_detection

@app.get("/image_detections/", response_model=list[schemas.ImageDetection])
def read_detections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_image_detections(db, skip=skip, limit=limit)

@app.put("/image_detections/{detection_id}", response_model=schemas.ImageDetection)
def update_detection(detection_id: int, detection: schemas.ImageDetectionCreate, db: Session = Depends(get_db)):
    return crud.update_image_detection(db, detection_id=detection_id, detection=detection)

@app.delete("/image_detections/{detection_id}")
def delete_detection(detection_id: int, db: Session = Depends(get_db)):
    detection = crud.delete_image_detection(db, detection_id=detection_id)
    if detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return {"message": "Detection deleted successfully"}
