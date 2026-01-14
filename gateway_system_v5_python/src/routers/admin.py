from fastapi import APIRouter, HTTPException
from src.models.route import Route
from src.services.route_service import RouteService

router = APIRouter(prefix="/admin")
service = RouteService()


@router.get("/routes")
async def get_routes():
    return service.get_all()


@router.post("/routes")
async def add_route(route: Route):
    return service.add(route)


@router.delete("/routes/{id}")
async def remove_route(id: str):
    service.remove(id)
    return {"status": "removed"}
