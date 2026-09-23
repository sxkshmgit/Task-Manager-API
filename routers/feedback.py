from enum import Enum
from typing import Annotated , Optional

from fastapi import APIRouter, Form , UploadFile
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
def submit_feedback(
    form: Annotated[FeedbackForm, Form()],
    attachment: Optional[UploadFile] = None,
):
    result = {
        "task_id": form.task_id,
        "rating": form.rating,
        "difficulty": form.difficulty,
        "feedback": form.feedback,
    }
    if attachment:
        result["filename"] = attachment.filename
        result["content_type"] = attachment.content_type
    return result