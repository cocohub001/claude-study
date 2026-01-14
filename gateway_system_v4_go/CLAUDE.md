# API Gateway - Go Implementation

## Project Overview

This is a modern API Gateway system built with **Go** following the complete Claude Code AI-assisted development workflow.

## Technology Stack

- **Language**: Go 1.21+
- **Framework**: Gin Web Framework
- **Build Tool**: Go Modules
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
gateway_system_v4_go/
├── CLAUDE.md                    # This file
├── .claude/
│   ├── skills/                  # Multi-file skills
│   ├── hooks/
│   ├── subagents/
│   └── commands/
├── mcp/                         # MCP server
│   └── gateway-mcp/
├── cmd/                         # Application entry points
│   └── gateway/
├── internal/                    # Private application code
│   ├── handler/
│   ├── model/
│   └── service/
├── go.mod
└── go.sum
```

## Development Guidelines

### Code Style
- Follow Effective Go guidelines
- Use gofmt for formatting
- Keep functions small and focused
- Use meaningful variable names

### Architecture Principles
- Clean Architecture
- Dependency Injection
- Interface-based design
- Error handling with wrapped errors

### Testing Requirements
- Unit tests for all business logic
- Integration tests for API endpoints
- Use table-driven tests

## Quick Start

### Build the Project
```bash
go build -o gateway ./cmd/gateway
```

### Run the Gateway
```bash
go run ./cmd/gateway
```

### Run Tests
```bash
go test ./...
```
