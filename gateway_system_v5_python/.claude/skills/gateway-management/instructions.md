# Gateway Management Instructions

## Route Operations

### Add Route
```bash
curl -X POST http://localhost:8000/admin/routes \
  -H "Content-Type: application/json" \
  -d '{"id":"users","path":"/api/users","backend":"http://localhost:3000"}'
```

### List Routes
```bash
curl http://localhost:8000/admin/routes
```

### Delete Route
```bash
curl -X DELETE http://localhost:8000/admin/routes/{id}
```

## Health Check
```bash
curl http://localhost:8000/health
```
