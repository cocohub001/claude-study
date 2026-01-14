from src.models.route import Route


class RouteService:
    def __init__(self):
        self.routes: dict[str, Route] = {}

    def get_all(self) -> list[Route]:
        return list(self.routes.values())

    def get(self, id: str) -> Route | None:
        return self.routes.get(id)

    def add(self, route: Route) -> Route:
        self.routes[route.id] = route
        return route

    def remove(self, id: str) -> None:
        self.routes.pop(id, None)

    def find_by_path(self, path: str) -> Route | None:
        for route in self.routes.values():
            if route.enabled and path.startswith(route.path):
                return route
        return None
