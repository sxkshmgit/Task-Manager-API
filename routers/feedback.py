from enum import Enum

from fastapi import APIRouter, Form

router = APIRouter(prefix="/feedback", tags=["Feedback"])


class Difficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


@router.post("")
def submit_feedback(
    task_id: int = Form(...),
    rating: int = Form(..., ge=1, le=5),
    difficulty: Difficulty = Form(...),
    feedback: str = Form(..., min_length=1, max_length=1000),
):
    return {
        "task_id": task_id,
        "rating": rating,
        "difficulty": difficulty,
        "feedback": feedback,
    }