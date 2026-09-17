import os
import tempfile
from runner_engine.core.local_runner import LocalRunner

def test_local_runner_basic_execution():
    runner = LocalRunner()
    
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(temp_dir, 'main.py')
        with open(script_path, 'w') as f:
            f.write("print('Hello from local runner')\n")
            
        result = runner.run_code(workspace_path=temp_dir, entry_file='main.py')
        
        assert result['status'] == 'COMPLETED'
        assert result['exit_code'] == 0
        assert 'Hello from local runner' in result['stdout']

def test_local_runner_error_execution():
    runner = LocalRunner()
    
    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = os.path.join(temp_dir, 'main.py')
        with open(script_path, 'w') as f:
            f.write("print(undefined_variable)\n")
            
        result = runner.run_code(workspace_path=temp_dir, entry_file='main.py')
        
        # It runs successfully but returns exit code 1
        assert result['status'] == 'COMPLETED'
        assert result['exit_code'] != 0
        assert 'NameError' in result['stderr']
