# import sys
# import os
# import traceback
# from typing import Any, List, Dict
# from mcp.server.fastmcp import FastMCP
# from github_integration import fetch_pr_changes
# from notion_client import Client
# from dotenv import load_dotenv


# class PRAnalyzer:
#     def __init__(self):
#         # Load environment variables
#         load_dotenv()

#         # Initialize MCP Server
#         self.mcp = FastMCP("github_pr_analysis")
#         print("MCP Server initialized", file=sys.stderr)

#         # Initialize Notion client
#         self._init_notion()

#         # Register MCP tools
#         self._register_tools()

#     def _init_notion(self):
#         """Initialize the Notion client with API key and page ID."""
#         try:
#             self.notion_api_key = os.getenv("NOTION_API_KEY")
#             self.notion_page_id = os.getenv("NOTION_PAGE_ID")

#             if not self.notion_api_key or not self.notion_page_id:
#                 raise ValueError(
#                     "Missing Notion API key or page ID in environment variables")

#             self.notion = Client(auth=self.notion_api_key)
#             print(f"Notion client initialized successfully", file=sys.stderr)
#             print(
#                 f"Using Notion page ID: {self.notion_page_id}", file=sys.stderr)
#         except Exception as e:
#             print(
#                 f"Error initializing Notion client: {str(e)}", file=sys.stderr)
#             traceback.print_exc(file=sys.stderr)
#             sys.exit(1)

#     def _register_tools(self):
#         """Register MCP tools for PR analysis."""
#         @self.mcp.tool()
#         async def fetch_pr(repo_owner: str, repo_name: str, pr_number: int) -> Dict[str, Any]:
#             """Fetch changes from a GitHub pull request."""
#             print(
#                 f"Fetching PR #{pr_number} from {repo_owner}/{repo_name}", file=sys.stderr)
#             try:
#                 pr_info = fetch_pr_changes(repo_owner, repo_name, pr_number)
#                 if pr_info is None:
#                     print("No changes returned from fetch_pr_changes",
#                           file=sys.stderr)
#                     return {}
#                 print(f"Successfully fetched PR information", file=sys.stderr)
#                 return pr_info
#             except Exception as e:
#                 print(f"Error fetching PR: {str(e)}", file=sys.stderr)
#                 traceback.print_exc(file=sys.stderr)
#                 return {}

#         @self.mcp.tool()
#         async def create_notion_page(title: str, content: str) -> str:
#             """Create a Notion page with PR analysis."""
#             print(f"Creating Notion page: {title}", file=sys.stderr)
#             try:
#                 self.notion.pages.create(
#                     parent={"type": "page_id", "page_id": self.notion_page_id},
#                     properties={
#                         "title": {"title": [{"text": {"content": title}}]}},
#                     children=[{
#                         "object": "block",
#                         "type": "paragraph",
#                         "paragraph": {
#                             "rich_text": [{
#                                 "type": "text",
#                                 "text": {"content": content}
#                             }]
#                         }
#                     }]
#                 )
#                 print(
#                     f"Notion page '{title}' created successfully!", file=sys.stderr)
#                 return f"Notion page '{title}' created successfully!"
#             except Exception as e:
#                 error_msg = f"Error creating Notion page: {str(e)}"
#                 print(error_msg, file=sys.stderr)
#                 traceback.print_exc(file=sys.stderr)
#                 return error_msg

#     def run(self):
#         """Start the MCP server."""
#         try:
#             print("Running MCP Server for GitHub PR Analysis...", file=sys.stderr)
#             self.mcp.run(transport="stdio")
#         except Exception as e:
#             print(f"Fatal Error in MCP Server: {str(e)}", file=sys.stderr)
#             traceback.print_exc(file=sys.stderr)
#             sys.exit(1)


# if __name__ == "__main__":
#     analyzer = PRAnalyzer()
#     analyzer.run()

# import sys
# import os
# import traceback
# from typing import Any, List, Dict
# from mcp.server.fastmcp import FastMCP
# from github_integration import fetch_pr_changes
# from notion_client import Client
# from dotenv import load_dotenv
# import uvicorn  # Add Uvicorn import


# class PRAnalyzer:
#     def __init__(self):
#         # Load environment variables
#         load_dotenv()

#         # Initialize MCP Server
#         self.mcp = FastMCP("github_pr_analysis")
#         print("MCP Server initialized", file=sys.stderr)

#         # Initialize Notion client
#         self._init_notion()

#         # Register MCP tools
#         self._register_tools()

#     def _init_notion(self):
#         """Initialize the Notion client with API key and page ID."""
#         try:
#             self.notion_api_key = os.getenv("NOTION_API_KEY")
#             self.notion_page_id = os.getenv("NOTION_PAGE_ID")

#             if not self.notion_api_key or not self.notion_page_id:
#                 raise ValueError(
#                     "Missing Notion API key or page ID in environment variables")

#             self.notion = Client(auth=self.notion_api_key)
#             print(f"Notion client initialized successfully", file=sys.stderr)
#             print(
#                 f"Using Notion page ID: {self.notion_page_id}", file=sys.stderr)
#         except Exception as e:
#             print(
#                 f"Error initializing Notion client: {str(e)}", file=sys.stderr)
#             traceback.print_exc(file=sys.stderr)
#             sys.exit(1)

#     def _register_tools(self):
#         """Register MCP tools for PR analysis."""
#         @self.mcp.tool()
#         async def fetch_pr(repo_owner: str, repo_name: str, pr_number: int) -> Dict[str, Any]:
#             """Fetch changes from a GitHub pull request."""
#             print(
#                 f"Fetching PR #{pr_number} from {repo_owner}/{repo_name}", file=sys.stderr)
#             try:
#                 pr_info = fetch_pr_changes(repo_owner, repo_name, pr_number)
#                 if pr_info is None:
#                     print("No changes returned from fetch_pr_changes",
#                           file=sys.stderr)
#                     return {}
#                 print(f"Successfully fetched PR information", file=sys.stderr)
#                 return pr_info
#             except Exception as e:
#                 print(f"Error fetching PR: {str(e)}", file=sys.stderr)
#                 traceback.print_exc(file=sys.stderr)
#                 return {}

#         @self.mcp.tool()
#         async def create_notion_page(title: str, content: str) -> str:
#             """Create a Notion page with PR analysis."""
#             print(f"Creating Notion page: {title}", file=sys.stderr)
#             try:
#                 self.notion.pages.create(
#                     parent={"type": "page_id",
#                             "page_id": self.notion_page_id},
#                     properties={
#                         "title": {"title": [{"text": {"content": title}}]}},
#                     children=[{
#                         "object": "block",
#                         "type": "paragraph",
#                         "paragraph": {
#                             "rich_text": [{
#                                 "type": "text",
#                                 "text": {"content": content}
#                             }]
#                         }
#                     }]
#                 )
#                 print(
#                     f"Notion page '{title}' created successfully!", file=sys.stderr)
#                 return f"Notion page '{title}' created successfully!"
#             except Exception as e:
#                 error_msg = f"Error creating Notion page: {str(e)}"
#                 print(error_msg, file=sys.stderr)
#                 traceback.print_exc(file=sys.stderr)
#                 return error_msg

#     def run(self):
#         """Start the MCP server with HTTP transport."""
#         try:
#             print(
#                 "Running MCP Server for GitHub PR Analysis over HTTP...", file=sys.stderr)
#             # Use Uvicorn to run the FastAPI app
#             uvicorn.run(
#                 self.mcp,  # FastMCP provides a FastAPI app
#                 host="0.0.0.0",
#                 # Use PORT env var or default to 8000
#                 port=int(os.getenv("PORT", 8000)),
#             )
#         except Exception as e:
#             print(f"Fatal Error in MCP Server: {str(e)}", file=sys.stderr)
#             traceback.print_exc(file=sys.stderr)
#             sys.exit(1)


# if __name__ == "__main__":
#     analyzer = PRAnalyzer()
#     analyzer.run()

# import sys
# import os
# import traceback
# from typing import Any, Dict
# from mcp.server.fastmcp import FastMCP
# from github_integration import fetch_pr_changes
# from notion_client import Client
# from dotenv import load_dotenv

# mcp = FastMCP("github_pr_analysis")
# print("MCP Server initialized - first", file=sys.stderr)


# class PRAnalyzer:
#     def __init__(self):
#         # Load environment variables
#         load_dotenv()

#         # Initialize MCP Server
#         self.mcp = FastMCP("github_pr_analysis")
#         print("MCP Server initialized", file=sys.stderr)

#         # Initialize Notion client
#         self._init_notion()

#         # Register MCP tools
#         self._register_tools()

#     def _init_notion(self):
#         """Initialize the Notion client with API key and page ID."""
#         try:
#             self.notion_api_key = os.getenv("NOTION_API_KEY")
#             self.notion_page_id = os.getenv("NOTION_PAGE_ID")

#             if not self.notion_api_key or not self.notion_page_id:
#                 raise ValueError(
#                     "Missing Notion API key or page ID in environment variables")

#             self.notion = Client(auth=self.notion_api_key)
#             print(f"Notion client initialized successfully", file=sys.stderr)
#             print(
#                 f"Using Notion page ID: {self.notion_page_id}", file=sys.stderr)
#         except Exception as e:
#             print(
#                 f"Error initializing Notion client: {str(e)}", file=sys.stderr)
#             traceback.print_exc(file=sys.stderr)
#             sys.exit(1)

#     def _register_tools(self):
#         """Register MCP tools for PR analysis."""
#         @self.mcp.tool()
#         async def fetch_pr(repo_owner: str, repo_name: str, pr_number: int) -> Dict[str, Any]:
#             """Fetch changes from a GitHub pull request."""
#             print(
#                 f"Fetching PR #{pr_number} from {repo_owner}/{repo_name}", file=sys.stderr)
#             try:
#                 pr_info = fetch_pr_changes(repo_owner, repo_name, pr_number)
#                 if pr_info is None:
#                     print("No changes returned from fetch_pr_changes",
#                           file=sys.stderr)
#                     return {}
#                 print(f"Successfully fetched PR information", file=sys.stderr)
#                 return pr_info
#             except Exception as e:
#                 print(f"Error fetching PR: {str(e)}", file=sys.stderr)
#                 traceback.print_exc(file=sys.stderr)
#                 return {}

#         @self.mcp.tool()
#         async def create_notion_page(title: str, content: str) -> str:
#             """Create a Notion page with PR analysis."""
#             print(f"Creating Notion page: {title}", file=sys.stderr)
#             try:
#                 self.notion.pages.create(
#                     parent={"type": "page_id", "page_id": self.notion_page_id},
#                     properties={
#                         "title": {"title": [{"text": {"content": title}}]}},
#                     children=[{
#                         "object": "block",
#                         "type": "paragraph",
#                         "paragraph": {
#                             "rich_text": [{
#                                 "type": "text",
#                                 "text": {"content": content}
#                             }]
#                         }
#                     }]
#                 )
#                 print(
#                     f"Notion page '{title}' created successfully!", file=sys.stderr)
#                 return f"Notion page '{title}' created successfully!"
#             except Exception as e:
#                 error_msg = f"Error creating Notion page: {str(e)}"
#                 print(error_msg, file=sys.stderr)
#                 traceback.print_exc(file=sys.stderr)
#                 return error_msg

#     def run(self):
#         """Start the MCP server with HTTP transport."""
#         try:
#             print(
#                 "Running MCP Server for GitHub PR Analysis over HTTP...", file=sys.stderr)
#             self.mcp.run(
#                 transport="streamable-http",

#             )

#         except Exception as e:
#             print(f"Fatal Error in MCP Server: {str(e)}", file=sys.stderr)
#             traceback.print_exc(file=sys.stderr)
#             sys.exit(1)


# if __name__ == "__main__":
#     analyzer = PRAnalyzer()
#     analyzer.run()
#

import sys
import os
import traceback
import json
from typing import Any, Dict
from mcp.server.fastmcp import FastMCP
from github_integration import fetch_pr_changes
from notion_client import Client
from dotenv import load_dotenv


class PRAnalyzer:
    def __init__(self):
        """Initialize the PR Analyzer with MCP server and Notion client."""
        load_dotenv()

        # Initialize MCP Server
        self.mcp = FastMCP("github_pr_analysis")
        print("MCP Server initialized", file=sys.stderr)

        # Initialize Notion client
        self._init_notion()

        # Register MCP tools
        self._register_tools()

    def _init_notion(self):
        """Initialize the Notion client with API key and page ID."""
        try:
            self.notion_api_key = os.getenv("NOTION_API_KEY")
            self.notion_page_id = os.getenv("NOTION_PAGE_ID")

            if not self.notion_api_key:
                print("Warning: NOTION_API_KEY not found in environment",
                      file=sys.stderr)
                self.notion = None
                return

            if not self.notion_page_id:
                print("Warning: NOTION_PAGE_ID not found in environment",
                      file=sys.stderr)
                self.notion = None
                return

            self.notion = Client(auth=self.notion_api_key)
            print("Notion client initialized successfully", file=sys.stderr)
            print(
                f"Using Notion page ID: {self.notion_page_id}", file=sys.stderr)

        except Exception as e:
            print(
                f"Error initializing Notion client: {str(e)}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            self.notion = None

    def _register_tools(self):
        """Register MCP tools for PR analysis."""
        try:
            @self.mcp.tool()
            async def fetch_pr(repo_owner: str, repo_name: str, pr_number: int) -> Dict[str, Any]:
                """Fetch changes from a GitHub pull request."""
                print(
                    f"Fetching PR #{pr_number} from {repo_owner}/{repo_name}", file=sys.stderr)
                try:
                    pr_info = fetch_pr_changes(
                        repo_owner, repo_name, pr_number)
                    if pr_info is None:
                        print("No changes returned from fetch_pr_changes",
                              file=sys.stderr)
                        return {"error": "Failed to fetch PR information"}

                    print("Successfully fetched PR information", file=sys.stderr)
                    return pr_info

                except Exception as e:
                    error_msg = f"Error fetching PR: {str(e)}"
                    print(error_msg, file=sys.stderr)
                    traceback.print_exc(file=sys.stderr)
                    return {"error": error_msg}

            @self.mcp.tool()
            async def create_notion_page(title: str, content: str) -> str:
                """Create a Notion page with PR analysis."""
                print(f"Creating Notion page: {title}", file=sys.stderr)

                if not self.notion:
                    error_msg = "Notion client not initialized. Check API key and page ID."
                    print(error_msg, file=sys.stderr)
                    return error_msg

                try:
                    # Split content into blocks if it's too long
                    content_blocks = []
                    if len(content) > 2000:
                        chunks = [content[i:i+2000]
                                  for i in range(0, len(content), 2000)]
                        for chunk in chunks:
                            content_blocks.append({
                                "object": "block",
                                "type": "paragraph",
                                "paragraph": {
                                    "rich_text": [{
                                        "type": "text",
                                        "text": {"content": chunk}
                                    }]
                                }
                            })
                    else:
                        content_blocks.append({
                            "object": "block",
                            "type": "paragraph",
                            "paragraph": {
                                "rich_text": [{
                                    "type": "text",
                                    "text": {"content": content}
                                }]
                            }
                        })

                    response = self.notion.pages.create(
                        parent={"type": "page_id",
                                "page_id": self.notion_page_id},
                        properties={
                            "title": {"title": [{"text": {"content": title}}]}
                        },
                        children=content_blocks
                    )

                    success_msg = f"Notion page '{title}' created successfully! Page ID: {response['id']}"
                    print(success_msg, file=sys.stderr)
                    return success_msg

                except Exception as e:
                    error_msg = f"Error creating Notion page: {str(e)}"
                    print(error_msg, file=sys.stderr)
                    traceback.print_exc(file=sys.stderr)
                    return error_msg

            print("MCP tools registered successfully", file=sys.stderr)

        except Exception as e:
            print(f"Error registering MCP tools: {str(e)}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)

    def run_stdio(self):
        """Run the MCP server with stdio transport (for MCP clients)."""
        try:
            print("Running MCP Server for GitHub PR Analysis via stdio...",
                  file=sys.stderr)
            self.mcp.run(transport="stdio")
        except Exception as e:
            print(f"Fatal Error in MCP Server: {str(e)}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)

    def run_http(self, host="127.0.0.1", port=8000):
        """Run the MCP server with HTTP transport using FastAPI and Uvicorn."""
        try:
            print(f"Starting MCP Server for GitHub PR Analysis...", file=sys.stderr)
            print(
                f"Server will be available at http://{host}:{port}", file=sys.stderr)

            # Import required packages
            try:
                import uvicorn
                from fastapi import FastAPI, HTTPException, Request
                from fastapi.middleware.cors import CORSMiddleware
                from fastapi.responses import JSONResponse, StreamingResponse
                import asyncio
            except ImportError as e:
                print(f"Required packages not installed: {e}", file=sys.stderr)
                print("Please install: pip install uvicorn fastapi", file=sys.stderr)
                sys.exit(1)

            # Create FastAPI app
            app = FastAPI(
                title="GitHub PR Analyzer MCP Server",
                description="MCP Server for analyzing GitHub Pull Requests and creating Notion pages",
                version="1.0.0"
            )

            # Add CORS middleware
            app.add_middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

            # Health check endpoint
            @app.get("/health")
            async def health_check():
                return {
                    "status": "healthy",
                    "service": "github_pr_analysis",
                    "endpoints": ["/health", "/mcp", "/tools"]
                }

            # List available tools
            # @app.get("/mcp")
            # async def list_tools():
            #     return {
            #         "tools": [
            #             {
            #                 "name": "fetch_pr",
            #                 "description": "Fetch changes from a GitHub pull request",
            #                 "parameters": ["repo_owner", "repo_name", "pr_number"]
            #             },
            #             {
            #                 "name": "create_notion_page",
            #                 "description": "Create a Notion page with PR analysis",
            #                 "parameters": ["title", "content"]
            #             }
            #         ]
            #     }
            @app.get("/mcp")
            async def list_tools(request: Request):
                """Handle MCP communication via Server-Sent Events."""
                async def event_generator():
                    tools = [
                        {
                            "name": "fetch_pr",
                            "description": "Fetch changes from a GitHub pull request",
                            "parameters": [
                                {"name": "repo_owner", "type": "string",
                                    "description": "Repository owner"},
                                {"name": "repo_name", "type": "string",
                                    "description": "Repository name"},
                                {"name": "pr_number", "type": "integer",
                                    "description": "Pull request number"}
                            ],
                            "language": "python",
                            "type": "tool"
                        },
                        {
                            "name": "create_notion_page",
                            "description": "Create a Notion page with PR analysis",
                            "parameters": [
                                {"name": "title", "type": "string",
                                    "description": "Page title"},
                                {"name": "content", "type": "string",
                                    "description": "Page content"}
                            ],
                            "language": "python",
                            "type": "tool"
                        }
                    ]
                    yield f"data: {json.dumps({'type': 'connected', 'server': 'github_pr_analysis', 'tools': tools})}\n\n"
                    # Keep the connection alive
                    while True:
                        if await request.is_disconnected():
                            break
                        yield "data: {}\n\n"  # Heartbeat to keep connection alive
                        await asyncio.sleep(30)

                return StreamingResponse(
                    event_generator(),
                    media_type="text/event-stream",
                    headers={
                        "Cache-Control": "no-cache",
                        "Connection": "keep-alive",
                        "Access-Control-Allow-Origin": "*",
                    }
                )

            # MCP endpoint for Server-Sent Events

            @app.get("/tools")
            async def mcp_endpoint(request: Request):
                """Handle MCP communication via Server-Sent Events."""
                def event_generator():
                    yield f"data: {json.dumps({'type': 'connected', 'server': 'github_pr_analysis'})}\n\n"

                return StreamingResponse(
                    event_generator(),
                    media_type="text/event-stream",
                    headers={
                        "Cache-Control": "no-cache",
                        "Connection": "keep-alive",
                        "Access-Control-Allow-Origin": "*",
                    }
                )

            # Direct tool endpoints for easier testing
            @app.post("/fetch_pr")
            async def fetch_pr_endpoint(
                repo_owner: str,
                repo_name: str,
                pr_number: int
            ):
                """Direct endpoint to fetch PR information."""
                try:
                    print(
                        f"Direct API call: Fetching PR #{pr_number} from {repo_owner}/{repo_name}", file=sys.stderr)
                    result = fetch_pr_changes(repo_owner, repo_name, pr_number)

                    if result is None:
                        return {"error": "Failed to fetch PR information"}

                    return result

                except Exception as e:
                    print(
                        f"Error in fetch_pr_endpoint: {str(e)}", file=sys.stderr)
                    raise HTTPException(status_code=500, detail=str(e))

            @app.post("/create_notion_page")
            async def create_notion_page_endpoint(title: str, content: str):
                """Direct endpoint to create Notion page."""
                if not self.notion:
                    raise HTTPException(
                        status_code=500,
                        detail="Notion client not configured. Check NOTION_API_KEY and NOTION_PAGE_ID environment variables."
                    )

                try:
                    print(
                        f"Direct API call: Creating Notion page '{title}'", file=sys.stderr)
                    result = await self._create_notion_page_impl(title, content)
                    return {"message": result}

                except Exception as e:
                    print(
                        f"Error in create_notion_page_endpoint: {str(e)}", file=sys.stderr)
                    raise HTTPException(status_code=500, detail=str(e))

            # Add some helpful documentation endpoints
            @app.get("/")
            async def root():
                return {
                    "message": "GitHub PR Analyzer MCP Server",
                    "version": "1.0.0",
                    "endpoints": {
                        "health": "/health - Server health check",
                        "tools": "/tools - List available tools",
                        "mcp": "/mcp - MCP Server-Sent Events endpoint",
                        "fetch_pr": "/fetch_pr - Direct PR fetching endpoint",
                        "create_notion_page": "/create_notion_page - Direct Notion page creation endpoint"
                    },
                    "example_usage": {
                        "fetch_pr": "POST /fetch_pr with repo_owner, repo_name, pr_number",
                        "create_notion_page": "POST /create_notion_page with title and content"
                    }
                }

            print(f"Endpoints configured:", file=sys.stderr)
            print(f"  - Health: http://{host}:{port}/health", file=sys.stderr)
            print(f"  - MCP: http://{host}:{port}/tool", file=sys.stderr)
            print(f"  - Tools: http://{host}:{port}/mcp", file=sys.stderr)
            print(
                f"  - Fetch PR: http://{host}:{port}/fetch_pr", file=sys.stderr)
            print(
                f"  - Create Notion: http://{host}:{port}/create_notion_page", file=sys.stderr)

            # Start the server
            uvicorn.run(
                app,
                host=host,
                port=port,
                log_level="info",
                access_log=True
            )

        except Exception as e:
            print(f"Fatal Error in HTTP MCP Server: {str(e)}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)

    async def _create_notion_page_impl(self, title: str, content: str):
        """Implementation of Notion page creation."""
        content_blocks = []

        if len(content) > 2000:
            chunks = [content[i:i+2000] for i in range(0, len(content), 2000)]
            for chunk in chunks:
                content_blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{
                            "type": "text",
                            "text": {"content": chunk}
                        }]
                    }
                })
        else:
            content_blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": content}
                    }]
                }
            })

        response = self.notion.pages.create(
            parent={"type": "page_id", "page_id": self.notion_page_id},
            properties={
                "title": {"title": [{"text": {"content": title}}]}
            },
            children=content_blocks
        )

        return f"Notion page '{title}' created successfully! Page ID: {response['id']}"


def main():
    """Main entry point with argument parsing."""
    analyzer = PRAnalyzer()

    # Parse command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--stdio":
            analyzer.run_stdio()
        elif sys.argv[1] == "--http":
            host = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
            port = int(sys.argv[3]) if len(sys.argv) > 3 else 8000
            analyzer.run_http(host, port)
        else:
            print(
                "Usage: python main.py [--stdio|--http] [host] [port]", file=sys.stderr)
            print("  --stdio: Run with stdio transport (default)", file=sys.stderr)
            print("  --http: Run with HTTP transport", file=sys.stderr)
            print("  host: Host to bind to (default: 127.0.0.1)", file=sys.stderr)
            print("  port: Port to bind to (default: 8000)", file=sys.stderr)
            sys.exit(1)
    else:
        # Default to HTTP for easier testing
        analyzer.run_http()


if __name__ == "__main__":
    main()
