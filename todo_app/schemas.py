import pydantic


class TaskIn(pydantic.BaseModel):
    title: str
    description: str = None

