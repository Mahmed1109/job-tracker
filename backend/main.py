from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
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

@app.get("/applications/overdue", response_model=List[schemas.JobApplicationResponse])
def get_overdue_applications(db: Session = Depends(get_db)):
    today = date.today()
    applications = db.query(models.JobApplication).filter(
        models.JobApplication.follow_up_date < today,
        models.JobApplication.status.notin_(["Offer", "Rejected"])
    ).all()
    return applications

@app.get("/applications/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(models.JobApplication).count()
    applied = db.query(models.JobApplication).filter(models.JobApplication.status == "Applied").count()
    interview = db.query(models.JobApplication).filter(models.JobApplication.status == "Interview").count()
    offer = db.query(models.JobApplication).filter(models.JobApplication.status == "Offer").count()
    rejected = db.query(models.JobApplication).filter(models.JobApplication.status == "Rejected").count()
    response_rate = round((interview + offer) / total * 100, 1) if total > 0 else 0

    return {
        "total_applications": total,
        "applied": applied,
        "interview": interview,
        "offer": offer,
        "rejected": rejected,
        "response_rate_percent": response_rate
    }

@app.get("/applications/", response_model=List[schemas.JobApplicationResponse])
def get_applications(
    status: Optional[str] = Query(None, description="Filter by status: Applied, Interview, Offer, Rejected"),
    db: Session = Depends(get_db)
):
    query = db.query(models.JobApplication)
    if status:
        query = query.filter(models.JobApplication.status == status)
    applications = query.all()
    return applications

@app.get("/applications/{application_id}", response_model=schemas.JobApplicationResponse)
def get_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(models.JobApplication).filter(
        models.JobApplication.id == application_id
    ).first()
    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

@app.put("/applications/{application_id}", response_model=schemas.JobApplicationResponse)
def update_application(application_id: int, updated: schemas.JobApplicationCreate, db: Session = Depends(get_db)):
    application = db.query(models.JobApplication).filter(
        models.JobApplication.id == application_id
    ).first()
    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    application.company = updated.company
    application.job_title = updated.job_title
    application.status = updated.status
    application.job_url = updated.job_url
    application.location = updated.location
    application.salary = updated.salary
    application.notes = updated.notes
    application.date_applied = updated.date_applied
    application.follow_up_date = updated.follow_up_date
    db.commit()
    db.refresh(application)
    return application

@app.delete("/applications/{application_id}")
def delete_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(models.JobApplication).filter(
        models.JobApplication.id == application_id
    ).first()
    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(application)
    db.commit()
    return {"message": f"Application {application_id} deleted successfully"}