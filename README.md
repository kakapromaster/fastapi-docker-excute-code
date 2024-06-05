# FastAPI Docker Execution Service

This FastAPI application allows you to execute code within a Docker container with specified resource constraints. The service accepts code and resource requirements, executes the code in a Docker container, and returns the output.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.8 or higher
- Docker
- pip (Python package installer)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/agiletom/fastapi-docker-excute-code.git
    cd fastapi-docker-excute-code
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Docker:**

    Follow the instructions on the [Docker website](https://docs.docker.com/get-docker/) to install Docker for your operating system.

## Running the Application

1. **Ensure Docker is running:**

    Make sure your Docker daemon is running. You can start it from the Docker Desktop application or use the command line.

2. **Start the FastAPI server:**

    ```bash
    uvicorn app.main:app --reload
    ```

    The server will start and be accessible at `http://127.0.0.1:8000`.

## API Usage

### Endpoint: Execute Task

- **URL:** `http://127.0.0.1:8000/execute`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
      "task_type": "execute_code",
      "code": "print('Hello, World!')",
      "resources": {
        "cpu": "2",
        "gpu": "0",
        "ram": "512MB",
        "storage": "1GB"
      }
    }
    ```

- **Response:**

    ```json
    {
        "output": "Hello, World!\n"
    }
    ```

### Example using Postman

1. **Open Postman** and create a new POST request.

2. **Set the URL** to `http://127.0.0.1:8000/execute`.

3. **Set the request body** to raw JSON:

    ```json
    {
      "task_type": "execute_code",
      "code": "print('Hello, World!')",
      "resources": {
        "cpu": "2",
        "gpu": "0",
        "ram": "512MB",
        "storage": "1GB"
      }
    }
    ```

4. **Send the request.**

5. **View the response** in the Postman response section. It should look like:

    ```json
    {
        "output": "Hello, World!\n"
    }
    ```
