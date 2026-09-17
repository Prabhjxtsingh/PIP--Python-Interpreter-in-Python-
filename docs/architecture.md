# System Architecture & Design

## 1. High-Level Architecture (Online Model)
- **Browser Frontend (React):** Houses the Monaco Editor, xterm.js terminal, and workspace UI.
- **API Layer (Django + DRF):** Manages users, projects, and execution requests.
- **WebSocket Channel (Django Channels + Redis):** Real-time I/O streaming for the terminal.
- **Job Queue (Celery + Redis/RabbitMQ):** Asynchronous task orchestration for code execution.
- **Execution Sandbox (Docker):** Ephemeral containers allocated per run to execute arbitrary user code securely.
- **Storage:** Postgres for relational data, S3-compatible storage for user uploaded files and scratch disks.

### Flow Diagram
Browser <--> Django/DRF API <--> Celery Workers <--> Docker Sandbox Pool <--> S3 / Postgres

## 2. High-Level Architecture (Offline Model)
- **Shared Runner Engine:** The core execution sandbox logic (handling resource limits, subprocessing) packaged as an internal Python library.
- **Local Application Shell:** pywebview or PyQt wrapping a local lightweight Python web server (Flask/Django-lite).
- **Execution Mode:** Uses lightweight subprocessing (or RestrictedPython) locally, with an option to utilize Docker if present.

## 3. Database Schema (Postgres)
- **User:** Authentication and profile info.
- **Project:** Workspace groupings (has one owner User).
- **File/Folder:** Tree structure representation of files within a Project.
- **ExecutionRun:** Tracks status, stdout, stderr, exit code, duration, and associated Project.
- **TerminalSession:** Logs for active or past interactive sessions.

## 4. Security & Threat Model
- **Isolation:** Every execution happens in an ephemeral container.
- **Resource Quotas:** CPU shares, memory cap, wall-clock timeouts, disk quotas, process count limits.
- **Network:** Disabled inside the sandbox by default.
- **Filesystem:** Read-only access to base environment, write access restricted to the temporary workspace volume.
- **Vulnerability Mitigation:** Drop dangerous syscalls via seccomp/AppArmor.
