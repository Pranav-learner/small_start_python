from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    status: str = "TODO"

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    status: str = "TODO"
    user_id: int | None = None

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    status: str | None = Field(default=None)

class TaskResponse(BaseModel):
    task_id: int
    title: str
    status: str
    user_id: int | None = None

    model_config = {
        "from_attributes": True
    }
