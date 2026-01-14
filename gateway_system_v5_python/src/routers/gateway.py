from fastapi import APIRouter, Request
import httpx

from src.routers.admin import service

router = APIRouter()


@router.api_route("/api/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(request: Request, path: str):
    full_path = f"/api/{path}"
    route = service.find_by_path(full_path)

    if not route:
        return {"error": "route not found"}

    target_url = f"{route.backend}{full_path}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=target_url
        )
        return response.json()
