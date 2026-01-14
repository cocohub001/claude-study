# API Gateway - Java Implementation

## Project Overview

This is a modern API Gateway system built with **Java** following the complete Claude Code AI-assisted development workflow.

## Technology Stack

- **Language**: Java 17+
- **Framework**: Spring Boot 3.x
- **Build Tool**: Maven
- **MCP**: Python MCP SDK (for AI integration)
- **Configuration**: YAML

## Development Workflow

This project demonstrates the complete Claude Code "vibe coding" workflow:

```
CLAUDE.md → Skills → Hooks → Subagents → Slash Commands → MCP → Implementation
```

### 1. CLAUDE.md (This File)
Project context and guidelines for Claude Code.

### 2. Skills (Multi-file Structure)
Modular capabilities organized in `.claude/skills/` directory.

### 3. Hooks
Automated actions triggered by Claude Code events.

### 4. Subagents
Specialized agents for specific tasks.

### 5. Slash Commands
Custom commands for common operations.

### 6. MCP Servers
AI-assisted gateway management.

## Project Structure

```
gateway_system_v3_java/
├── CLAUDE.md                    # This file
├── .claude/
│   ├── skills/                  # Multi-file skills
│   │   ├── gateway-management/
│   │   │   ├── skill.md
│   │   │   ├── instructions.md
│   │   │   └── examples/
│   │   └── java-development/
│   │       ├── skill.md
│   │       ├── instructions.md
│   │       └── examples/
│   ├── hooks/                   # Event hooks
│   │   └── hooks.yaml
│   ├── subagents/              # Specialized agents
│   │   └── subagents.yaml
│   └── commands/               # Slash commands
│       └── commands.yaml
├── mcp/                        # MCP server
│   └── gateway-mcp/
├── src/                        # Java source code
│   └── main/
│       └── java/
│           └── com/gateway/
└── pom.xml                     # Maven configuration
```

## Development Guidelines

### Code Style
- Follow Google Java Style Guide
- Use meaningful variable and method names
- Add Javadoc comments for public APIs
- Keep methods small and focused

### Architecture Principles
- Clean Architecture (Domain → Application → Infrastructure)
- Dependency Injection via Spring
- Interface-based design
- Immutable objects where possible

### Testing Requirements
- Unit tests for all business logic
- Integration tests for API endpoints
- Minimum 80% code coverage

## Quick Start

### Build the Project
```bash
mvn clean install
```

### Run the Gateway
```bash
mvn spring-boot:run
```

### Run Tests
```bash
mvn test
```

## AI-Assisted Development

### Using Skills
Skills are invoked automatically when relevant tasks are detected.

### Using Hooks
Hooks run automatically on specific events (e.g., before commit, after build).

### Using Subagents
Subagents handle specialized tasks like code review, testing, documentation.

### Using Slash Commands
Type `/gateway` commands for quick gateway operations.

## Key Components

### Gateway Core
- Request routing and proxying
- Load balancing
- Circuit breaker pattern

### Middleware
- Authentication (JWT, API Key)
- Rate limiting
- Logging and monitoring

### Configuration
- YAML-based configuration
- Hot reload support
- Environment-specific profiles
