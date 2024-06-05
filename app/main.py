from fastapi import FastAPI, HTTPException
from app.schemas import TaskRequest, TaskResponse

app = FastAPI()

@app.post("/execute", response_model=TaskResponse)
async def execute_task(task_request: TaskRequest):
    try:
        result = "success"
        return TaskResponse(output=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))