from pydantic import BaseModel


class Route(BaseModel):
    id: str
    path: str
    backend: str
    methods: list[str] = ["GET"]
    enabled: bool = True
