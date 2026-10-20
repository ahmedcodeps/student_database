import secrets
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, Field

app = FastAPI(title="Student Results API")
security = HTTPBasic()

# Demo credentials 
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    valid_user = secrets.compare_digest(credentials.username, "teacher")
    valid_password = secrets.compare_digest(credentials.password, "demo123")

    if not (valid_user and valid_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


# Pydantic validation models
class ScoreCreate(BaseModel):
    student_id: int = Field(gt=0)
    assessment_id: int = Field(gt=0)
    score: float = Field(ge=0)


class ScoreUpdate(BaseModel):
    score: float = Field(ge=0)


# Example data stored in memory
students = {
    101: "Aisha Rahman",
    102: "Omar Nasser",
}

subjects = {
    1: {"id": 1, "name": "Mathematics"},
    2: {"id": 2, "name": "Science"},
}

assessments = {
    1: {
        "id": 1,
        "name": "Algebra Quiz",
        "subject_id": 1,
        "max_score": 100,
    },
    2: {
        "id": 2,
        "name": "Science Test",
        "subject_id": 2,
        "max_score": 50,
    },
    3: {
        "id": 3,
        "name": "Geometry Test",
        "subject_id": 1,
        "max_score": 100,
    },
}

# Key: (student_id, assessment_id)
scores = {
    (101, 1): 88.0,
    (102, 2): 42.0,
}


def check_student(student_id):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")


def check_score(score, assessment_id):
    if assessment_id not in assessments:
        raise HTTPException(status_code=404, detail="Assessment not found")

    if score > assessments[assessment_id]["max_score"]:
        raise HTTPException(
            status_code=422,
            detail="Score cannot exceed the assessment maximum",
        )


def format_result(student_id, assessment_id, score):
    assessment = assessments[assessment_id]
    subject = subjects[assessment["subject_id"]]

    return {
        "student_id": student_id,
        "student_name": students[student_id],
        "assessment_id": assessment_id,
        "assessment_name": assessment["name"],
        "subject": subject["name"],
        "score": score,
        "max_score": assessment["max_score"],
    }


@app.get("/subjects", dependencies=[Depends(authenticate)])
def get_subjects():
    return list(subjects.values())


@app.get("/assessments", dependencies=[Depends(authenticate)])
def get_assessments():
    return [
        {
            **assessment,
            "subject": subjects[assessment["subject_id"]]["name"],
        }
        for assessment in assessments.values()
    ]


@app.post("/scores", dependencies=[Depends(authenticate)])
def add_score(data: ScoreCreate):
    check_student(data.student_id)
    check_score(data.score, data.assessment_id)

    key = (data.student_id, data.assessment_id)

    if key in scores:
        raise HTTPException(
            status_code=409,
            detail="A score already exists for this student and assessment",
        )

    scores[key] = data.score
    return format_result(data.student_id, data.assessment_id, data.score)


@app.put(
    "/scores/{student_id}/{assessment_id}",
    dependencies=[Depends(authenticate)],
)
def update_score(student_id: int, assessment_id: int, data: ScoreUpdate):
    check_student(student_id)
    check_score(data.score, assessment_id)

    key = (student_id, assessment_id)

    if key not in scores:
        raise HTTPException(status_code=404, detail="Score not found")

    scores[key] = data.score
    return format_result(student_id, assessment_id, data.score)


@app.get("/students/{student_id}/results", dependencies=[Depends(authenticate)])
def get_results(student_id: int):
    check_student(student_id)

    return [
        format_result(sid, aid, score)
        for (sid, aid), score in scores.items()
        if sid == student_id
    ]


@app.get("/students/{student_id}/average", dependencies=[Depends(authenticate)])
def get_average(student_id: int):
    check_student(student_id)

    results = [
        score / assessments[aid]["max_score"] * 100
        for (sid, aid), score in scores.items()
        if sid == student_id
    ]

    if not results:
        raise HTTPException(status_code=404, detail="No scores found")

    return {
        "student_id": student_id,
        "student_name": students[student_id],
        "average_percentage": round(sum(results) / len(results), 2),
    }