import docker
import asyncio
import concurrent.futures
from app.schemas import TaskRequest

async def execute_code_in_docker(task_request: TaskRequest) -> str:
    """
    Executes the provided Python code in a Docker container.

    Args:
        task_request (TaskRequest): An object containing the code to execute and resource constraints.
                                    The TaskRequest schema should include:
                                    - code: The Python code to be executed as a string.
                                    - resources: An object specifying the resource limits for the container.
                                      - cpu (str): CPU quota in units of 1e-9 CPUs.
                                      - gpu (str): Number of GPUs to allocate for the container (e.g., "1" for one GPU, "0" if no GPU is needed).
                                      - ram (str): Maximum RAM limit for the container (e.g., "512MB").
                                      - storage (str): Storage limit for the container (e.g., "1GB").

    Returns:
        str: The output of the executed code from the Docker container logs.
    """
    # Initialize Docker client
    client = docker.DockerClient(base_url='tcp://localhost:2375')
    
    # Run the Docker container with the specified resource constraints
    container = client.containers.run(
        "python:3.8-slim",
        command=["python", "-c", task_request.code],
        detach=True,
        mem_limit=task_request.resources.ram,
        nano_cpus=int(task_request.resources.cpu),
        shm_size=task_request.resources.storage,
        device_requests=[docker.types.DeviceRequest(
            count=int(task_request.resources.gpu) if int(task_request.resources.gpu) > 0 else -1,
            capabilities=[["gpu"]]
        )]
    )
    
    # Wait for the container to finish execution
    container.wait()
    
    output = ""
    
    # Use a ThreadPoolExecutor to read logs asynchronously
    with concurrent.futures.ThreadPoolExecutor() as pool:
        loop = asyncio.get_event_loop()
        logs = await loop.run_in_executor(pool, lambda: list(container.logs(stream=True)))
    
    # Decode and accumulate logs from the container
    for log in logs:
        output += log.decode("utf-8")
    
    # Remove the container after execution
    container.remove()
    
    return output
