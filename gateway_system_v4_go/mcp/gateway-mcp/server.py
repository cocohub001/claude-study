"""
Gateway MCP Server for Go Gateway

Provides AI-assisted management for the Go API Gateway.
"""

import asyncio
import json
from typing import Any, Sequence
import httpx

from mcp.server import Server
from mcp.types import Resource, Tool, TextContent
import mcp.server.stdio


# Configuration
GATEWAY_URL = "http://localhost:8080"

# Create MCP server
server = Server("go-gateway-mcp")


@server.list_resources()
async def list_resources() -> list[Resource]:
    """List available resources"""
    return [
        Resource(
            uri="gateway://routes",
            name="Gateway Routes",
            description="All configured routes",
            mimeType="application/json"
        ),
        Resource(
            uri="gateway://health",
            name="Gateway Health",
            description="Health status",
            mimeType="application/json"
        ),
        Resource(
            uri="gateway://metrics",
            name="Gateway Metrics",
            description="Performance metrics",
            mimeType="application/json"
        )
    ]


@server.read_resource()
async def read_resource(uri: str) -> str:
    """Read a resource from the Go gateway"""
    async with httpx.AsyncClient() as client:
        try:
            if uri == "gateway://routes":
                response = await client.get(f"{GATEWAY_URL}/admin/routes")
                return response.text
            elif uri == "gateway://health":
                response = await client.get(f"{GATEWAY_URL}/health")
                return response.text
            elif uri == "gateway://metrics":
                response = await client.get(f"{GATEWAY_URL}/metrics")
                return response.text
            else:
                raise ValueError(f"Unknown resource: {uri}")
        except httpx.RequestError as e:
            return json.dumps({"error": str(e)})


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools"""
    return [
        Tool(
            name="add_route",
            description="Add a new route",
            inputSchema={
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "path": {"type": "string"},
                    "backend": {"type": "string"},
                    "methods": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["id", "path", "backend"]
            }
        ),
        Tool(
            name="remove_route",
            description="Remove a route",
            inputSchema={
                "type": "object",
                "properties": {"id": {"type": "string"}},
                "required": ["id"]
            }
        ),
        Tool(
            name="get_health",
            description="Get health status",
            inputSchema={"type": "object", "properties": {}}
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent]:
    """Execute a tool"""
    async with httpx.AsyncClient() as client:
        try:
            if name == "add_route":
                route_data = {
                    "id": arguments["id"],
                    "path": arguments["path"],
                    "backend": arguments["backend"],
                    "methods": arguments.get("methods", ["GET"]),
                    "enabled": True
                }
                response = await client.post(
                    f"{GATEWAY_URL}/admin/routes",
                    json=route_data
                )
                return [TextContent(type="text", text=f"Route added: {response.text}")]

            elif name == "remove_route":
                route_id = arguments["id"]
                await client.delete(f"{GATEWAY_URL}/admin/routes/{route_id}")
                return [TextContent(type="text", text=f"Route removed: {route_id}")]

            elif name == "get_health":
                response = await client.get(f"{GATEWAY_URL}/health")
                return [TextContent(type="text", text=response.text)]

            else:
                return [TextContent(type="text", text=f"Unknown tool: {name}")]

        except httpx.RequestError as e:
            return [TextContent(type="text", text=f"Error: {str(e)}")]


async def main():
    """Run the MCP server"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
