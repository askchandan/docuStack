# DocuStack

A multi-container backend application built using Docker and Docker Compose, demonstrating service orchestration, networking, and persistent storage.

## Tech Stack
- Python (FastAPI)
- PostgreSQL
- Redis
- Docker & Docker Compose

## Architecture Overview

- The application is structured as a multi-service system managed using Docker Compose. Each service runs in its own container and communicates over a shared Docker network.

- The API service acts as the entry point and exposes HTTP endpoints. It communicates internally with the PostgreSQL database for data persistence and with Redis for caching and fast connectivity checks.

- Docker Compose automatically creates an isolated network where services can discover each other using service names as hostnames. Persistent storage for the database is handled using a named Docker volume to ensure data durability across container restarts.


## Services

### API Service
- Built using FastAPI (Python)
- Exposes HTTP endpoints for health and connectivity checks
- Connects to PostgreSQL and Redis using internal Docker networking
- Containerized using a custom Dockerfile

### PostgreSQL Service
- Uses the official PostgreSQL image
- Stores application data persistently using a named Docker volume
- Configured via environment variables loaded from a `.env` file

### Redis Service
- Uses the official Redis image
- Acts as an in-memory data store for fast connectivity validation
- Runs as an internal service without exposing ports to the host

## How to Run

### Prerequisites
- Docker
- Docker Compose

### Steps to Run the Application

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd docustack

2. Build and start all services using Docker Compose:
   ```bash
    docker compose up --build

3. Access the API in the browser:
   ```bash
    http://localhost:8000
- A successful response confirms that the API, PostgreSQL, and Redis services are running and connected.

4. To stop and remove the containers:
   ```bash
    docker compose down


📌 Why this is strong:
- Uses real commands you actually ran
- Clean, minimal, reproducible
- Signals “this project works on any machine”

---

## Docker Concepts Demonstrated

- Containerization of a Python API using a custom Dockerfile
- Multi-container orchestration using Docker Compose
- Service-to-service communication using Docker’s internal network
- Use of environment variables and `.env` files for configuration
- Persistent data storage using named Docker volumes
- Dependency management between services using `depends_on`
- Use of official Docker images for PostgreSQL and Redis
- Container lifecycle management using `docker compose up` and `down`
- Image build optimization using `.dockerignore`
- Debugging and inspection using Docker logs and exec commands
