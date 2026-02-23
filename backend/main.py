from fastapi import FastAPI

app = FastAPI(title="Job Application Tracker", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}