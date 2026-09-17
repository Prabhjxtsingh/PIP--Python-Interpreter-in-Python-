# Execution Runner Engine

The unner_engine is the core library that powers code execution.

## DockerRunner
Used by the Online Web Platform.
Spawns ephemeral python:3.12-slim containers.
Imposes strict resource limits:
- Network disabled
- 128MB Memory Limit

## LocalRunner
Used by the Offline Desktop Application.
Executes code natively using Python's subprocess without sandbox constraints, since the user is operating within their own trusted environment.
