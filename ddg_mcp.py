import asyncio
from duckduckgo_search import DDGS
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

app = Server("duckduckgo-search")

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="web_search",
            description="Search the web using DuckDuckGo. Returns titles, URLs, and text snippets.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to search the web for"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default 5)"
                    }
                },
                "required": ["query"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name != "web_search":
        raise ValueError(f"Unknown tool: {name}")

    query = arguments.get("query")
    if not query:
        raise ValueError("Missing required argument: query")
        
    max_results = arguments.get("max_results", 5)

    try:
        results = DDGS().text(query, max_results=max_results)
        output = ""
        for i, res in enumerate(results):
            output += f"[{i+1}] {res.get('title', 'No Title')}\n"
            output += f"URL: {res.get('href', 'No URL')}\n"
            output += f"Snippet: {res.get('body', 'No Snippet')}\n\n"
            
        if not output:
            output = "No results found."
            
        return [TextContent(type="text", text=output)]
    except Exception as e:
        return [TextContent(type="text", text=f"Search failed: {str(e)}")]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
