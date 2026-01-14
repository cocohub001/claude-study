# API Gateway - Python Implementation

## Project Overview

This is a modern API Gateway system built with **Python** following the complete Claude Code AI-assisted development workflow.

## Technology Stack

- **Language**: Python 3.11+
- **Framework**: FastAPI
- **Async**: asyncio + httpx
- **MCP**: Python MCP SDK

## Development Workflow

```
CLAUDE.md → Skills → Hooks → Subagents → Slash Commands → MCP → Implementation
```

## Project Structure

```
gateway_system_v5_python/
├── CLAUDE.md
├── .claude/
│   ├── skills/
│   ├── hooks/
│   ├── subagents/
│   └── commands/
├── mcp/gateway-mcp/
├── src/
│   ├── main.py
│   ├── models/
│   ├── services/
│   └── routers/
├── requirements.txt
└── README.md
```

## Development Guidelines

### Code Style
- Follow PEP 8
- Use type hints
- Async/await for I/O operations
- Docstrings for public functions
