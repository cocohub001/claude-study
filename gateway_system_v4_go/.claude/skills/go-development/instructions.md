# Go Development Instructions

## Handler Pattern

```go
func (h *Handler) GetRoutes(c *gin.Context) {
    routes := h.service.GetAllRoutes()
    c.JSON(http.StatusOK, routes)
}
```

## Service Pattern

```go
type RouteService struct {
    routes map[string]*Route
    mu     sync.RWMutex
}

func (s *RouteService) GetAllRoutes() []*Route {
    s.mu.RLock()
    defer s.mu.RUnlock()
    // return routes
}
```

## Testing Pattern

```go
func TestGetRoutes(t *testing.T) {
    tests := []struct {
        name     string
        expected int
    }{
        {"empty", 0},
        {"with routes", 2},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            // test logic
        })
    }
}
```
