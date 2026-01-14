# Java API Gateway - Version 3

A complete Java API Gateway implementation with AI-assisted development workflow.

## Quick Start

### Prerequisites
- Java 17+
- Maven 3.8+
- Python 3.10+ (for MCP server)

### Build and Run

```bash
# Build the project
mvn clean install

# Run the gateway
mvn spring-boot:run
```

### Install MCP Dependencies

```bash
cd mcp/gateway-mcp
pip install -r requirements.txt
```

## Project Structure

```
gateway_system_v3_java/
├── CLAUDE.md                 # AI context
├── .claude/
│   ├── skills/               # Multi-file skills
│   ├── hooks/                # Event hooks
│   ├── subagents/            # Specialized agents
│   ├── commands/             # Slash commands
│   └── mcp.json              # MCP configuration
├── mcp/gateway-mcp/          # MCP server
├── src/main/java/com/gateway/
│   ├── GatewayApplication.java
│   ├── model/Route.java
│   ├── service/RouteService.java
│   └── controller/
│       ├── AdminController.java
│       └── GatewayController.java
└── pom.xml
```
