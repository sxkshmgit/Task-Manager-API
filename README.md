# Task Manager API

A full-stack Task Manager built with **Python, FastAPI, Pydantic, REST APIs, CRUD operations, validation, filtering, sorting, headers, form handling, file uploads, and CORS**.

## Features

- Create, read, update, partially update, and delete tasks
- Pydantic request and response validation
- Task status and priority enums
- Search tasks by title
- Filter tasks by status and priority
- Sort tasks by title, due date, priority, or creation time
- Automatic task creation and update timestamps
- HTTP error handling with `HTTPException`
- Header parameters and reusable header models
- User creation endpoint with Pydantic validation
- Task feedback endpoint using Form Data and a Pydantic Form Model
- Optional file upload support with `UploadFile`
- Interactive Swagger/OpenAPI documentation
- HTML/CSS/JavaScript frontend with Task Feedback UI
- CORS support for frontend-to-API requests

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
    ├── tasks.py
    ├── users.py
    └── feedback.py
```

## Run Locally

Create and activate a virtual environment, then install the project dependencies:

```bash
pip install "fastapi[standard]" python-multipart
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

### Tasks

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/tasks` | List tasks with search/filter/sort |
| GET | `/tasks/{task_id}` | Get a task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{task_id}` | Replace a task |
| PATCH | `/tasks/{task_id}` | Partially update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

### Users

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/users` | Create a user |

### Feedback

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/feedback` | Submit task feedback using form fields with an optional file upload |

## Tech Stack

- Python
- FastAPI
- Pydantic
- HTML
- CSS
- JavaScript

## Current Storage

Task and user data are currently stored **in memory**, so they are cleared when the API restarts. Feedback submissions are validated and returned by the API but are not persisted. Uploaded files are currently accepted and their filename/content type are returned, but files are not persisted to storage.

A database, authentication, persistent file storage, and other production-oriented features can be added as future development steps.
