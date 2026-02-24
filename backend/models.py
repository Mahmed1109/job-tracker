from sqlalchemy import Column, Integer, String, Text, Date, DateTime
from sqlalchemy.sql import func
from backend.database import Base

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(100), nullable=False)
    job_title = Column(String(100), nullable=False)
    status = Column(String(50), default="Applied")
    job_url = Column(String(500), nullable=True)
    location = Column(String(100), nullable=True)
    salary = Column(String(50), nullable=True)
    notes = Column(Text, nullable=True)
    date_applied = Column(Date, nullable=True)
    follow_up_date = Column(Date, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())