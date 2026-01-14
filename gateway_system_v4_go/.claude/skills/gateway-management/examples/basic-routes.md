# Example: Basic Route Management

## Add a Route

```
User: Add a route for the users API
Claude: [Uses gateway-management skill]
```

**Command:**
```bash
curl -X POST http://localhost:8080/admin/routes \
  -d '{"id":"users","path":"/api/users","backend":"http://localhost:3001"}'
```

## Check Health

```
User: Is the gateway healthy?
Claude: [Checks health endpoint]
```

**Response:**
```json
{"status": "healthy", "uptime": "2h30m"}
```
