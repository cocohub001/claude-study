# Example: Basic Route Management

## Scenario
Set up routes for a microservices architecture with user and product services.

## Steps

### 1. Add User Service Route
```
User: Add a route for the user service at /api/users/* pointing to http://localhost:8001
Claude: [Uses gateway-management skill]
        ✓ Route 'user-service' added successfully
```

### 2. Add Product Service Route
```
User: Add a route for products at /api/products/* to http://localhost:8002
Claude: [Uses gateway-management skill]
        ✓ Route 'product-service' added successfully
```

### 3. Verify Routes
```
User: List all routes
Claude: [Uses gateway-management skill]
        Found 2 routes:
        - user-service: /api/users/* -> http://localhost:8001
        - product-service: /api/products/* -> http://localhost:8002
```

### 4. Check Health
```
User: Is the gateway healthy?
Claude: [Uses gateway-management skill]
        Gateway Status: Healthy
        - Active routes: 2
        - Error rate: 0.1%
        - Avg latency: 45ms
```
