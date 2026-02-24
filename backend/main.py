from fastapi import FastAPI
from backend.database import engine
from backend import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Tracker", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}