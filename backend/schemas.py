from pydantic import BaseModel
from typing import Optional
from datetime import date

class JobApplicationCreate(BaseModel):
    company: str
    job_title: str
    status: Optional[str] = "Applied"
    job_url: Optional[str] = None
    location: Optional[str] = None
    salary: Optional[str] = None
    notes: Optional[str] = None
    date_applied: Optional[date] = None
    follow_up_date: Optional[date] = None

class JobApplicationResponse(JobApplicationCreate):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True