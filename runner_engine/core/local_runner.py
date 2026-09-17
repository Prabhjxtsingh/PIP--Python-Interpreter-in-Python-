import subprocess
import os

class LocalRunner:
    def __init__(self):
        pass

    def run_code(self, workspace_path: str, entry_file: str, timeout: int = 10):
        """
        Runs Python code locally using subprocess.
        WARNING: This does NOT provide sandbox isolation. It is meant for the offline desktop app 
        where the user is running code on their own trusted machine.
        """
        try:
            target_file = os.path.join(workspace_path, entry_file)
            result = subprocess.run(
                ["python", target_file],
                cwd=workspace_path,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            return {
                "status": "COMPLETED",
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except subprocess.TimeoutExpired as e:
            return {
                "status": "FAILED",
                "exit_code": -1,
                "error": "Execution timed out"
            }
        except Exception as e:
            return {
                "status": "FAILED",
                "exit_code": -1,
                "error": str(e)
            }
