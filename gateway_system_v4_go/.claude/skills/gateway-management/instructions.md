# Gateway Management Instructions

## Route Operations

### Add Route
```bash
curl -X POST http://localhost:8080/admin/routes \
  -H "Content-Type: application/json" \
  -d '{"id":"users","path":"/api/users","backend":"http://users-service:3000"}'
```

### List Routes
```bash
curl http://localhost:8080/admin/routes
```

### Delete Route
```bash
curl -X DELETE http://localhost:8080/admin/routes/{id}
```

## Health Monitoring

### Check Health
```bash
curl http://localhost:8080/health
```

### View Metrics
```bash
curl http://localhost:8080/metrics
```
