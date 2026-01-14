# Example: Creating Go Components

## Create a Handler

```
User: Create a route handler
Claude: [Uses go-development skill]
```

**Generated Code:**
```go
type RouteHandler struct {
    service *RouteService
}

func NewRouteHandler(s *RouteService) *RouteHandler {
    return &RouteHandler{service: s}
}
```

## Create a Service

```
User: Create a route service
Claude: [Uses go-development skill]
```

**Generated Code:**
```go
type RouteService struct {
    routes map[string]*Route
    mu     sync.RWMutex
}
```
