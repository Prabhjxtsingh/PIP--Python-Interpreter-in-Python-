from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
from runner_engine.core.local_runner import LocalRunner

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

static_dir = os.path.join(get_base_path(), 'static')
app = Flask(__name__, static_folder=static_dir, static_url_path='')
CORS(app)

WORKSPACE_DIR = os.path.join(os.path.expanduser('~'), 'PIP_Workspace')
os.makedirs(WORKSPACE_DIR, exist_ok=True)

@app.route('/')
def serve_index():
    return send_from_directory(static_dir, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    if os.path.exists(os.path.join(static_dir, path)):
        return send_from_directory(static_dir, path)
    return send_from_directory(static_dir, 'index.html')

@app.route('/api/run', methods=['POST'])
def run_code():
    data = request.json
    entry_file = data.get('entry_file')
    
    if not entry_file:
        return jsonify({"error": "entry_file is required"}), 400
        
    runner = LocalRunner()
    result = runner.run_code(workspace_path=WORKSPACE_DIR, entry_file=entry_file)
    
    return jsonify(result)

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"})

def start_server(port=5000):
    app.run(host='127.0.0.1', port=port, threaded=True)
