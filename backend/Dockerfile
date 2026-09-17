FROM python:3.12-slim

# Install docker CLI for the DockerRunner (though SDK might suffice, good to have)
RUN apt-get update && apt-get install -y docker.io

WORKDIR /app

# Install runner_engine first
COPY runner_engine /runner_engine
RUN pip install -e /runner_engine

# Install backend dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY backend /app

EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "config.asgi:application"]
