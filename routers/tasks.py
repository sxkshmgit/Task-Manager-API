from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException

from models import Task, TaskCreate, TaskUpdate, Priority, Status

router = APIRouter(prefix="/tasks", tags=["Tasks"])

tasks: dict[int, Task] = {}
next_id = 1


def now() -> str:
    return datetime.utcnow().isoformat()


@router.get("", response_model=list[Task])
def get_tasks(
    search: str = "",
    status: Optional[Status] = None,
    priority: Optional[Priority] = None,
    sort_by: str = "created_at",
):
    result = list(tasks.values())

    if search:
        result = [t for t in result if search.lower() in t.title.lower()]

    if status:
        result = [t for t in result if t.status == status]

    if priority:
        result = [t for t in result if t.priority == priority]

    if sort_by in ["title", "due_date", "priority", "created_at"]:
        result.sort(key=lambda t: getattr(t, sort_by) or "")

    return result


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    global next_id
    new_task = Task(id=next_id, created_at=now(), updated_at=now(), **task.dict())
    tasks[next_id] = new_task
    next_id += 1
    return new_task


@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    existing = tasks[task_id]
    updated = Task(id=task_id, created_at=existing.created_at, updated_at=now(), **task.dict())
    tasks[task_id] = updated
    return updated


@router.patch("/{task_id}", response_model=Task)
def patch_task(task_id: int, changes: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    data = tasks[task_id].dict()
    data.update(changes.dict(exclude_unset=True))
    data["updated_at"] = now()
    updated = Task(**data)
    tasks[task_id] = updated
    return updated


@router.delete("/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted"}
