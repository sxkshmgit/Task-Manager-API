from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import tasks , users, feedback

app = FastAPI(title="Task Manager API" , version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router)
app.include_router(users.router)
app.include_router(feedback.router)
