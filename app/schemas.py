from pydantic import BaseModel

class ResourceRequirements(BaseModel):
    """
    Resource requirements for the Docker container.

    Attributes:
        cpu (str): CPU quota in units of 1e-9 CPUs.
        gpu (str): Number of GPUs to allocate for the container (e.g., "1" for one GPU, "0" if no GPU is needed).
        ram (str): Maximum RAM limit for the container (e.g., "512MB").
        storage (str): Storage limit for the container (e.g., "1GB").
    """
    cpu: str
    gpu: str
    ram: str
    storage: str
