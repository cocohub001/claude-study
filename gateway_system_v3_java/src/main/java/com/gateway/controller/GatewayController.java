package com.gateway.controller;

import com.gateway.model.Route;
import com.gateway.service.RouteService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

import jakarta.servlet.http.HttpServletRequest;

@RestController
@RequestMapping("/api")
public class GatewayController {

    private final RouteService routeService;
    private final WebClient webClient;

    public GatewayController(RouteService routeService) {
        this.routeService = routeService;
        this.webClient = WebClient.create();
    }

    @RequestMapping("/**")
    public Mono<ResponseEntity<String>> proxy(HttpServletRequest request) {
        String path = request.getRequestURI();
        String method = request.getMethod();

        return routeService.findRouteByPath(path)
                .map(route -> forwardRequest(route, path, method))
                .orElse(Mono.just(ResponseEntity.notFound().build()));
    }

    private Mono<ResponseEntity<String>> forwardRequest(
            Route route, String path, String method) {
        String targetUrl = route.getBackend() + path;

        return webClient.method(
                org.springframework.http.HttpMethod.valueOf(method))
                .uri(targetUrl)
                .retrieve()
                .bodyToMono(String.class)
                .map(ResponseEntity::ok)
                .onErrorReturn(ResponseEntity.internalServerError()
                        .body("Gateway error"));
    }
}
