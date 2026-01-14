# Java Development Instructions

## Code Generation

### Creating a Service Class
```
User: Create a RouteService class for managing routes
Claude: [Uses java-development skill]
        Generated RouteService.java with:
        - CRUD operations
        - Dependency injection
        - Proper exception handling
```

### Creating a Controller
```
User: Create a REST controller for routes
Claude: [Uses java-development skill]
        Generated RouteController.java with:
        - RESTful endpoints
        - Request validation
        - Response DTOs
```

## Spring Boot Patterns

### Constructor Injection (Preferred)
```java
@Service
public class RouteService {
    private final RouteRepository repository;

    public RouteService(RouteRepository repository) {
        this.repository = repository;
    }
}
```

### Configuration Properties
```java
@ConfigurationProperties(prefix = "gateway")
public record GatewayProperties(
    int port,
    int timeout,
    int maxConnections
) {}
```

## Testing Guidelines

- Use `@SpringBootTest` for integration tests
- Use `@WebMvcTest` for controller tests
- Mock dependencies with `@MockBean`
