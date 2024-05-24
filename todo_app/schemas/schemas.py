import pydantic


class TaskIn(pydantic.BaseModel): # валидация данных при создании задачи
    title: str
    description: str = None
