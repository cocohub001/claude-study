package com.gateway.service;

import com.gateway.model.Route;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class RouteService {

    private final Map<String, Route> routes = new ConcurrentHashMap<>();

    public List<Route> getAllRoutes() {
        return new ArrayList<>(routes.values());
    }

    public Optional<Route> getRoute(String id) {
        return Optional.ofNullable(routes.get(id));
    }

    public Route addRoute(Route route) {
        routes.put(route.getId(), route);
        return route;
    }

    public void removeRoute(String id) {
        routes.remove(id);
    }

    public Optional<Route> findRouteByPath(String path) {
        return routes.values().stream()
                .filter(Route::isEnabled)
                .filter(r -> path.startsWith(r.getPath()))
                .findFirst();
    }

    public void reloadRoutes() {
        // Placeholder for configuration reload
    }
}
