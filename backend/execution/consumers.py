import json
from channels.generic.websocket import WebsocketConsumer
import docker
import threading
import os

class TerminalConsumer(WebsocketConsumer):
    def connect(self):
        self.project_id = self.scope['url_route']['kwargs']['project_id']
        # Accept the connection
        self.accept()
        
        # Connect to Docker and spin up a shell
        self.client = docker.from_env()
        try:
            self.container = self.client.containers.run(
                'python:3.12-slim',
                command='/bin/bash',
                stdin_open=True,
                tty=True,
                detach=True,
                network_disabled=True,
                mem_limit="128m",
                # volume mount for workspace goes here
            )
            
            # Attach to the socket to read/write
            self.socket = self.container.attach_socket(params={'stdin': 1, 'stdout': 1, 'stderr': 1, 'stream': 1})
            
            # Start a thread to read from docker and write to websocket
            self.running = True
            self.read_thread = threading.Thread(target=self._read_from_docker)
            self.read_thread.start()
            
            self.send(text_data="\r\nConnected to PIP Sandbox.\r\n")
        except Exception as e:
            self.send(text_data=f"\r\nError connecting to sandbox: {str(e)}\r\n")
            self.close()

    def disconnect(self, close_code):
        self.running = False
        try:
            if hasattr(self, 'socket'):
                self.socket.close()
            if hasattr(self, 'container'):
                self.container.remove(force=True)
        except:
            pass

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            if hasattr(self, 'socket'):
                # Send user input to the docker container
                self.socket._sock.send(text_data.encode('utf-8'))

    def _read_from_docker(self):
        try:
            while self.running:
                data = self.socket._sock.recv(4096)
                if not data:
                    break
                self.send(text_data=data.decode('utf-8', errors='replace'))
        except Exception as e:
            pass
