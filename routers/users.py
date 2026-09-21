from fastapi import APIRouter

from models import User, UserCreate

router = APIRouter(prefix="/users", tags=["Users"])

users: dict[int, User] = {}
next_id = 1


@router.post("", response_model=User, status_code=201)
def create_user(user: UserCreate):
    global next_id
    new_user = User(id=next_id, **user.dict())
    users[next_id] = new_user
    next_id += 1
    return new_user