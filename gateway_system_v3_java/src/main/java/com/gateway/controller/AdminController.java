package com.gateway.controller;

import com.gateway.model.Route;
import com.gateway.service.RouteService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/admin")
public class AdminController {

    private final RouteService routeService;

    public AdminController(RouteService routeService) {
        this.routeService = routeService;
    }

    @GetMapping("/routes")
    public List<Route> getAllRoutes() {
        return routeService.getAllRoutes();
    }

    @GetMapping("/routes/{id}")
    public ResponseEntity<Route> getRoute(@PathVariable String id) {
        return routeService.getRoute(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping("/routes")
    public Route addRoute(@RequestBody Route route) {
        return routeService.addRoute(route);
    }

    @DeleteMapping("/routes/{id}")
    public ResponseEntity<Void> removeRoute(@PathVariable String id) {
        routeService.removeRoute(id);
        return ResponseEntity.noContent().build();
    }

    @PostMapping("/routes/reload")
    public ResponseEntity<String> reloadRoutes() {
        routeService.reloadRoutes();
        return ResponseEntity.ok("Routes reloaded");
    }
}
