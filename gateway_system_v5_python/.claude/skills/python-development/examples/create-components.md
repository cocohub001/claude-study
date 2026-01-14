# Example: Creating Components

## Create a Router
```python
router = APIRouter(prefix="/users")

@router.get("/")
async def list_users():
    return service.get_all()
```
