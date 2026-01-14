# Python Development Instructions

## Router Pattern
```python
from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/items")
async def get_items():
    return []
```

## Service Pattern
```python
class RouteService:
    def __init__(self):
        self.routes = {}

    def get_all(self):
        return list(self.routes.values())
```
