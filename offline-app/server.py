from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from runner_engine.core.local_runner import LocalRunner

app = Flask(__name__)
CORS(app)

# A simple workspace directory for the offline app (e.g., in the user's Documents folder)
WORKSPACE_DIR = os.path.join(os.path.expanduser('~'), 'PIP_Workspace')
os.makedirs(WORKSPACE_DIR, exist_ok=True)

@app.route('/api/run', methods=['POST'])
def run_code():
    data = request.json
    entry_file = data.get('entry_file')
    
    if not entry_file:
        return jsonify({"error": "entry_file is required"}), 400
        
    runner = LocalRunner()
    # In offline mode, the user works directly in their local workspace
    result = runner.run_code(workspace_path=WORKSPACE_DIR, entry_file=entry_file)
    
    return jsonify(result)

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"})

def start_server(port=5000):
    # Running threaded so it doesn't block the UI
    app.run(host='127.0.0.1', port=port, threaded=True)
