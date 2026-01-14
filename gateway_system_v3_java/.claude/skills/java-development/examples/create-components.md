# Example: Creating Gateway Components

## Create a Route Entity

```
User: Create a Route entity class
Claude: [Uses java-development skill]
```

**Generated Code:**
```java
@Entity
@Table(name = "routes")
public class Route {
    @Id
    private String id;
    private String path;
    private String backend;
    private List<String> methods;
    private boolean enabled;

    // Getters, setters, builder pattern
}
```

## Create a Route Service

```
User: Create a service for route management
Claude: [Uses java-development skill]
```

**Generated Code:**
```java
@Service
@Transactional
public class RouteService {
    private final RouteRepository repository;

    public RouteService(RouteRepository repository) {
        this.repository = repository;
    }

    public Route addRoute(RouteRequest request) {
        // Implementation
    }
}
```
