from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.database import engine, SessionLocal
from backend import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Tracker", version="1.0.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}

@app.post("/applications/", response_model=schemas.JobApplicationResponse)
def create_application(application: schemas.JobApplicationCreate, db: Session = Depends(get_db)):
    db_application = models.JobApplication(
        company=application.company,
        job_title=application.job_title,
        status=application.status,
        job_url=application.job_url,
        location=application.location,
        salary=application.salary,
        notes=application.notes,
        date_applied=application.date_applied,
        follow_up_date=application.follow_up_date
    )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

@app.get("/applications/", response_model=List[schemas.JobApplicationResponse])
def get_applications(db: Session = Depends(get_db)):
    applications = db.query(models.JobApplication).all()
    return applications