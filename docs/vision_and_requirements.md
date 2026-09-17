# PIP: Product Vision & Requirements

## 1. Product Vision
PIP (Python Interpreter in Python) is an end-to-end Python Compiler/IDE providing a seamless coding experience. It targets students, interview candidates, development teams, and hobbyists. It bridges the gap between web-based coding environments and local desktop applications by offering:
- **Model 1 (Online):** A cloud-powered web application allowing users to write, run, and manage Python projects entirely in the browser.
- **Model 2 (Offline):** A downloadable desktop package that mirrors the online feature set but executes code securely on the user's local machine.

## 2. Functional Requirements
- **Code Execution:** Securely run Python code files and complete projects.
- **File/Workspace Management:** Upload, organize, and manage files and folders (drag-and-drop, tree view).
- **Interactive Terminal:** Provide a browser-based terminal emulator for real-time interaction (e.g., input(), shell commands).
- **Offline Availability:** Allow users to download a standalone desktop version of the IDE that operates locally without network latency for execution.
- **Dependency Management:** Support equirements.txt for installing third-party packages inside the execution sandbox.

## 3. Non-Functional Requirements
- **Security:** Strict sandboxing for untrusted user code (ephemeral containers, CPU/memory limits, no host filesystem access).
- **Latency & Concurrency:** Real-time terminal I/O via WebSockets. Ability to scale sandboxed execution workers based on load.
- **Code Reusability:** The sandboxed execution engine must be designed as a shared library (unner_engine) used by both the Django backend and the offline desktop application.
- **Portability:** Desktop application must be compatible with Windows, macOS, and Linux.

## 4. Feasibility & Risk Study
- **Risk 1: Executing Untrusted Code.** (High) Addressed by running every execution in network-isolated, resource-limited Docker containers.
- **Risk 2: Abuse/Resource Exhaustion.** (Medium) Addressed via strict CPU, memory, time quotas, and per-user rate limiting.
- **Risk 3: Maintaining Feature Parity.** (Medium) Addressed by wrapping the same Python unner_engine core in both the Django API and the local PyQt/pywebview shell.
