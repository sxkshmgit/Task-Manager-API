from datetime import datetime
from typing import Annotated, Optional
from database import SessionDep
from routers.users import get_current_user

from fastapi import APIRouter, HTTPException, Header , Depends , Query
from sqlmodel import select
from models import Task, TaskCreate, TaskUpdate, Priority, Status, TaskHeaders , User

router = APIRouter(prefix="/tasks", tags=["Tasks"])



def now() -> str:
    return datetime.utcnow().isoformat()

def common_params(search: str = "", sort_by: str = "created_at"):
    return {"search": search, "sort_by": sort_by}

@router.get("", response_model=list[Task])
def get_tasks(
    session: SessionDep,
    params: Annotated[dict, Depends(common_params)],
    current_user: Annotated[User, Depends(get_current_user)],
    status: Optional[Status] = None,
    priority: Optional[Priority] = None,
    headers: Annotated[TaskHeaders, Header()] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
):
    result = session.exec(select(Task)).all()

    if params["search"]:
        result = [t for t in result if params["search"].lower() in t.title.lower()]

    if status:
        result = [t for t in result if t.status == status]

    if priority:
        result = [t for t in result if t.priority == priority]

    if params["sort_by"] in ["title", "due_date", "priority", "created_at"]:
        result.sort(key=lambda t: getattr(t, params["sort_by"]) or "")

    start = (page - 1) * limit
    result = result[start:start + limit]

    return result


@router.get("/{task_id}", response_model=Task)
def get_task(
    task_id: int,
    session: SessionDep,
    current_user: Annotated[User, Depends(get_current_user)],
    headers: Annotated[TaskHeaders, Header()] = None,
):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("", response_model=Task, status_code=201)
def create_task(
    task: TaskCreate,
    session : SessionDep,
    current_user: Annotated[User, Depends(get_current_user)],
    headers: Annotated[TaskHeaders, Header()] = None,
):

    new_task = Task(created_at=now(), updated_at=now(), **task.dict())
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task


@router.put("/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task: TaskCreate,
    session: SessionDep,
    current_user: Annotated[User, Depends(get_current_user)],
    headers: Annotated[TaskHeaders, Header()] = None,
):
    existing = session.get(Task, task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict().items():
        setattr(existing, key, value)
    existing.updated_at = now()
    session.add(existing)
    session.commit()
    session.refresh(existing)
    return existing


@router.patch("/{task_id}", response_model=Task)
def patch_task(
    task_id: int,
    changes: TaskUpdate,
    session: SessionDep,
    current_user: Annotated[User, Depends(get_current_user)],
    headers: Annotated[TaskHeaders, Header()] = None,
):
    existing = session.get(Task, task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in changes.dict(exclude_unset=True).items():
        setattr(existing, key, value)
    existing.updated_at = now()

    session.add(existing)
    session.commit()
    session.refresh(existing)
    return existing


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    session: SessionDep,
    current_user: Annotated[User, Depends(get_current_user)],
    headers: Annotated[TaskHeaders, Header()] = None,
):
    existing = session.get(Task, task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")

    session.delete(existing)
    session.commit()
    return {"message": "Task deleted"}