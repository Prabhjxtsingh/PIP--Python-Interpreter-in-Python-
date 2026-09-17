from celery import shared_task
from .models import ExecutionRun
from runner_engine.core.docker_runner import DockerRunner
import os
from django.conf import settings

@shared_task
def execute_code(run_id, entry_file):
    try:
        run = ExecutionRun.objects.get(id=run_id)
        run.status = 'RUNNING'
        run.save()

        # In a real scenario, this is the dir where files are saved/mounted
        # Assuming the project files are mapped into a specific directory:
        workspace_path = os.path.join(settings.MEDIA_ROOT, 'projects', str(run.project.id))
        
        # Ensure dir exists for now so Docker doesn't crash on mount
        os.makedirs(workspace_path, exist_ok=True)
        
        runner = DockerRunner()
        result = runner.run_code(workspace_path=workspace_path, entry_file=entry_file)
        
        run.status = result.get('status')
        run.exit_code = result.get('exit_code')
        run.stdout = result.get('output', '') if run.status == 'COMPLETED' else ''
        run.stderr = result.get('error', '') if run.status == 'FAILED' else ''
        run.save()
        
    except ExecutionRun.DoesNotExist:
        pass
    except Exception as e:
        run.status = 'FAILED'
        run.stderr = str(e)
        run.save()
