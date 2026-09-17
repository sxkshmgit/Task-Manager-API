# Task Manager API

A full-stack Task Manager built to practice **Python, FastAPI, Pydantic, REST APIs, CRUD operations, validation, filtering, sorting, and CORS**.

## Features

- Create, read, update, partially update, and delete tasks
- Pydantic request/response validation
- Task status and priority enums
- Search tasks by title
- Filter by status and priority
- Sort by title, due date, priority, or creation time
- Automatic creation and update timestamps
- HTTP error handling with `HTTPException`
- Interactive Swagger/OpenAPI documentation
- Simple HTML/JavaScript frontend

## Screenshots

### Task Manager UI

![Task Manager UI](screenshots/Screenshot%202026-09-17%20145241.png)

### Swagger API Documentation

![Swagger API Documentation](screenshots/Screenshot%202026-09-17%20144941.png)

## Project Structure

```text
Task-Manager-API/
├── main.py
├── models.py
├── index.html
├── screenshots/
└── routers/
    ├── __init__.py
    └── tasks.py
```

## Run Locally

Create and activate a virtual environment, then install FastAPI:

```bash
pip install "fastapi[standard]"
```

Start the API:

```bash
fastapi dev main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

To serve the frontend from the project directory:

```bash
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500/index.html
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/tasks` | List tasks with search/filter/sort |
| GET | `/tasks/{task_id}` | Get a task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{task_id}` | Replace a task |
| PATCH | `/tasks/{task_id}` | Partially update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Tech Stack

- Python
- FastAPI
- Pydantic
- HTML
- CSS
- JavaScript

> Note: Task data is currently stored in memory, so data is cleared when the API restarts. A database can be added as the next development step.
