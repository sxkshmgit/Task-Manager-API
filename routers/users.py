from fastapi import APIRouter
from pwdlib import PasswordHash

from database import SessionDep
from models import User, UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["Users"])

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


@router.post("", response_model=UserRead, status_code=201)
def create_user(user: UserCreate, session: SessionDep):
    hashed_password = hash_password(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user