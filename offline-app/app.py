import webview
import threading
import time
import requests
import sys
import os
from server import start_server

def get_base_path():
    # If running inside PyInstaller executable, use _MEIPASS, else current dir
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def wait_for_server(port):
    """Wait until the Flask server is responsive."""
    url = f'http://127.0.0.1:{port}/api/ping'
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                break
        except requests.ConnectionError:
            pass
        time.sleep(0.1)

if __name__ == '__main__':
    port = 5000
    
    # Start the Flask server in a background thread
    t = threading.Thread(target=start_server, kwargs={'port': port})
    t.daemon = True
    t.start()
    
    # Wait for the backend to come up
    wait_for_server(port)
    
    # Point to the local Flask server which serves the static UI
    ui_url = f'http://127.0.0.1:{port}/'
    
    # Create the native window
    webview.create_window('PIP IDE', ui_url, width=1280, height=800)
    
    # Start the pywebview event loop
    webview.start(debug=False)
