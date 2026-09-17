import docker
import os

class DockerRunner:
    def __init__(self):
        self.client = docker.from_env()

    def run_code(self, workspace_path: str, entry_file: str, timeout: int = 10):
        """
        Runs Python code inside a secure Docker container.
        """
        try:
            container = self.client.containers.run(
                image="python:3.12-slim",
                command=f"python {entry_file}",
                volumes={
                    os.path.abspath(workspace_path): {
                        'bind': '/workspace',
                        'mode': 'ro'
                    }
                },
                working_dir="/workspace",
                mem_limit="128m",
                nano_cpus=1000000000, # 1 CPU
                network_disabled=True,
                detach=True,
                # In a real environment, you'd add AppArmor profiles, drop privileges, etc.
            )
            
            # Wait for execution or timeout
            result = container.wait(timeout=timeout)
            
            logs = container.logs().decode('utf-8')
            
            container.remove()
            
            return {
                "status": "COMPLETED",
                "exit_code": result.get("StatusCode"),
                "output": logs
            }
        except Exception as e:
            return {
                "status": "FAILED",
                "exit_code": -1,
                "error": str(e)
            }
