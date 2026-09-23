from enum import Enum
from typing import Annotated

from fastapi import APIRouter, Form
from pydantic import BaseModel, Field

router = APIRouter(prefix="/feedback", tags=["Feedback"])


class Difficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class FeedbackForm(BaseModel):
    task_id: int
    rating: int = Field(..., ge=1, le=5)
    difficulty: Difficulty
    feedback: str = Field(..., min_length=1, max_length=1000)


@router.post("")
def submit_feedback(form: Annotated[FeedbackForm, Form()]):
    return {
        "task_id": form.task_id,
        "rating": form.rating,
        "difficulty": form.difficulty,
        "feedback": form.feedback,
    }