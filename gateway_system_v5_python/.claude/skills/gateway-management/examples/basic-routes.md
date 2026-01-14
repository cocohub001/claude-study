# Example: Basic Route Management

## Add a Route
```bash
curl -X POST http://localhost:8000/admin/routes \
  -d '{"id":"users","path":"/api/users","backend":"http://localhost:3001"}'
```

## Check Health
```bash
curl http://localhost:8000/health
# Response: {"status": "healthy"}
```
