# API Specification Outline

This is a preliminary outline for the OpenAPI specification.

## Authentication
- \POST /api/auth/register\: Create a new user account.
- \POST /api/auth/login\: Authenticate and receive a token (JWT/Session).
- \POST /api/auth/logout\: Invalidate the current session.

## Projects & Workspaces
- \GET /api/projects\: List user's projects.
- \POST /api/projects\: Create a new project.
- \GET /api/projects/{id}\: Retrieve project details and root file tree.
- \DELETE /api/projects/{id}\: Delete a project.

## File Management
- \POST /api/projects/{id}/files\: Upload a file or folder (supports chunked upload).
- \GET /api/projects/{id}/files/{file_id}\: Download or view a file.
- \PUT /api/projects/{id}/files/{file_id}\: Rename or move a file/folder.
- \DELETE /api/projects/{id}/files/{file_id}\: Delete a file/folder.

## Code Execution
- \POST /api/projects/{id}/run\: Trigger execution of an entry file.
  - Payload: \{ "entry_file": "main.py" }\
  - Response: Queues a Celery task, returns \{ "run_id": "uuid" }\
- \GET /api/projects/{id}/run/{run_id}\: Poll execution status, stdout, stderr, duration.

## WebSockets
- \WS /ws/terminal/{project_id}\: Full-duplex channel connecting the xterm.js frontend to the backend sandbox shell.
