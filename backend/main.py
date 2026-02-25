from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.database import engine, SessionLocal
from backend import models

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