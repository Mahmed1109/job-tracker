# Job Application Tracker

A full-stack web application to track job applications, monitor statuses,
set follow-up reminders, and visualise your job search pipeline.

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **Frontend:** HTML, CSS, Vanilla JavaScript

## Features

- Add, edit and delete job applications
- Track status (Applied, Interview, Offer, Rejected)
- Follow-up reminder dates with overdue detection
- Dashboard with live stats and progress bars
- Search by company name or job title
- Filter by application status
- Colour coded status badges
- Response rate calculation

## Project Structure

```
job-tracker/
├── backend/
│   ├── main.py        # FastAPI app and all endpoints
│   ├── models.py      # Database models
│   ├── schemas.py     # Pydantic schemas
│   └── database.py    # Database connection
├── frontend/
│   └── index.html     # Frontend UI
├── requirements.txt
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Mahmed1109/job-tracker.git
cd job-tracker
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the backend server

```bash
uvicorn backend.main:app --reload
```

### 5. Open the frontend

Open `frontend/index.html` in your browser.

### 6. API Documentation

Visit `http://127.0.0.1:8000/docs` for the auto-generated API docs.

## API Endpoints

| Method | Endpoint              | Description              |
| ------ | --------------------- | ------------------------ |
| GET    | /applications/        | Get all applications     |
| POST   | /applications/        | Add a new application    |
| GET    | /applications/{id}    | Get a single application |
| PUT    | /applications/{id}    | Update an application    |
| DELETE | /applications/{id}    | Delete an application    |
| GET    | /applications/stats   | Get dashboard stats      |
| GET    | /applications/overdue | Get overdue follow ups   |

## Status

✅ Complete

```

---

**2. Update `requirements.txt`**
```

fastapi
uvicorn
sqlalchemy
pydantic
python-multipart

```

---

**3. Create a `.gitignore` file in the root `job-tracker` folder**
```

.venv/
**pycache**/
_.pyc
_.db
.DS_Store
