# Student Results API

## Purpose

A beginner FastAPI project for managing subjects, assessments, and student scores.

## Setup

Install Python 3, then open this folder in VS Code.

Create and activate a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

Install the required packages:

    pip install -r requirements.txt

## Run

Start the API:

    uvicorn main:app --reload

Open the API documentation:

    http://127.0.0.1:8000/docs

Use the Authorize option with:

- Username: teacher
- Password: demo123

## Endpoints

- GET /subjects
- GET /assessments
- POST /scores
- PUT /scores/{student_id}/{assessment_id}
- GET /students/{student_id}/results
- GET /students/{student_id}/average

## Validation and Security

Pydantic checks that IDs are positive and scores are not negative.
The API also rejects scores above the assessment maximum.

Basic authentication prevents requests without the demo credentials.
The API uses clear HTTP errors for missing records, duplicate scores,
invalid values, and failed authentication.

## Limitations

Data is stored in memory and resets when the server restarts.
The demo credentials are hard-coded and are not suitable for real student
records. A real system needs secure credentials, HTTPS, and persistent
storage with access controls.