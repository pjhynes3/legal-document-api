# Legal Document Management API

## Goal

This project is a personal learning project based on a backend interview exercise.

The purpose is **not** just to complete CRUD operations, but to understand how a real backend application is structured, how requests flow through the application, and why each layer exists.

---

# High-Level Architecture

```text
Client
    │
    ▼
FastAPI (API Layer)
    │
    ▼
Document Service (Business Logic)
    │
    ▼
Storage Layer
    │
    ▼
Database (Dictionary for this project)
```

For this project, the "database" is simply a Python dictionary stored in memory.

---

# Layers

### API Layer (`solution.py`)

Responsibilities:

* Receive HTTP requests
* Validate request format
* Call the appropriate service method
* Return HTTP responses
* Return appropriate status codes (200, 404, 400, etc.)

---

### Service Layer (`document_service.py`)

Responsibilities:

* Business logic
* Validation
* Caching
* Status transition rules
* Calling the storage layer

This layer answers the question:

> "Should this operation be allowed?"

---

### Storage Layer (`storage.py`)

Responsibilities:

* Create documents
* Read documents
* Update documents
* Delete documents
* List documents

This layer answers the question:

> "How do we store and retrieve data?"

---

# Glossary

| Term                   | Meaning                                                         |
| ---------------------- | --------------------------------------------------------------- |
| Architecture           | The overall organization of an application.                     |
| Layer                  | A section of the application with a single responsibility.      |
| API Layer              | Receives HTTP requests and returns HTTP responses.              |
| Service Layer          | Contains business rules and application logic.                  |
| Storage Layer          | Responsible for creating, reading, updating, and deleting data. |
| Separation of Concerns | Each layer should have one clear responsibility.                |
| CRUD                   | Create, Read, Update, Delete operations.                        |

---

# Guiding Question

Whenever writing code, ask:

> **Whose responsibility is this?**

Examples:

* Receive an HTTP request → API Layer
* Validate business rules → Service Layer
* Save data → Storage Layer
* Retrieve data → Storage Layer
* Return HTTP status codes → API Layer

---

# Notes

(To be filled in as I learn.)
