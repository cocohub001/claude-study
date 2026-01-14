# Gateway Management Instructions

## How to Use This Skill

### Adding a Route

When you need to add a new route, provide:
1. Route ID (unique identifier)
2. Path pattern (e.g., `/api/v1/*`)
3. Backend URL (e.g., `http://localhost:8001`)
4. HTTP methods (optional, defaults to GET, POST)

**Example prompt:**
```
Add a route called "user-service" that forwards /api/users/* to http://localhost:8001
```

### Removing a Route

Specify the route ID to remove:

**Example prompt:**
```
Remove the route "user-service"
```

### Listing Routes

**Example prompt:**
```
Show me all configured routes
```

### Checking Health

**Example prompt:**
```
What's the current health status of the gateway?
```

## Best Practices

1. **Use descriptive route IDs** - Makes management easier
2. **Group related routes** - Use consistent path prefixes
3. **Monitor regularly** - Check health and metrics frequently
4. **Test before production** - Verify routes work correctly

## Common Issues

### Route Not Found
- Verify the route ID exists
- Check for typos in the path

### Backend Unreachable
- Verify backend service is running
- Check network connectivity
- Verify the backend URL is correct
