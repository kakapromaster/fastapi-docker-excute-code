import docker
import asyncio
import concurrent.futures
from app.schemas import TaskRequest

async def execute_code_in_docker(task_request: TaskRequest) -> str:
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
