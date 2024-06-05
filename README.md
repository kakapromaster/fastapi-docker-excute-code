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

## Solution Explanation

### Overview

This FastAPI application provides a service to execute code inside a Docker container with specified resource constraints. The main goal is to ensure that the code runs in a controlled environment with allocated resources for CPU, GPU, RAM, and storage, thereby providing isolation and reproducibility.

### Components

1. **FastAPI**: The web framework used to build the API endpoints.
2. **Docker**: The containerization platform used to create isolated environments for code execution.
3. **Pydantic**: Used for data validation and settings management.

### Execution Flow

1. **API Request**: The client sends a POST request to the `/execute` endpoint with the code and resource constraints.
2. **Request Validation**: The request payload is validated against the `TaskRequest` schema to ensure it contains the required fields and correct data types.
3. **Docker Container Execution**: The `execute_code_in_docker` function handles the code execution inside a Docker container with the specified resource constraints.
4. **Resource Allocation**:
    - **CPU**: Allocated using the `nano_cpus` parameter.
    - **GPU**: Specified using `device_requests` with Docker's `DeviceRequest`.
    - **RAM**: Limited using the `mem_limit` parameter.
    - **Storage**: Constrained using the `shm_size` parameter.
5. **Log Retrieval**: The output logs from the container are retrieved and returned in the API response.
6. **Response**: The API response is structured according to the `TaskResponse` schema and sent back to the client with the execution output.

### Detailed Steps

1. **Clone the Repository**: This step involves getting the codebase onto your local machine.
2. **Set Up Virtual Environment**: A virtual environment is created to manage dependencies.
3. **Install Dependencies**: The required packages are installed using `pip`.
4. **Docker Installation**: Docker needs to be installed and running on your machine to create and manage containers.
5. **Start the FastAPI Server**: The application is started using Uvicorn, making the API accessible locally.

## Project Structure

```plaintext
.
├── app
│   ├── main.py
│   ├── schemas.py
│   └── docker_utils.py
├── requirements.txt
├── README.md
```

## Main application files

- `main.py`: Contains the FastAPI application and endpoint definitions.
- `docker_utils.py`: Contains the utility functions for executing code inside Docker containers.
- `schemas.py`: Defines the request and response schemas used for data validation.

## Suggested enhancements

1. **Support for More Languages**: Extend the `task_type` to support more programming languages like Javascript and Java.
2. **Enhanced Security**: Use the `sanitize-py` library to sanitize input code, ensuring that potentially malicious code is safely handled and cannot harm the host system.