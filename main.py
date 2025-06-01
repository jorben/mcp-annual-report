import uvicorn
from dotenv import load_dotenv
from fastmcp import FastMCP
from fastmcp.server.http import create_streamable_http_app
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.responses import PlainTextResponse

from middleware.auth import BearerAuthMiddleware
from tools import register_tools

load_dotenv()
mcp = FastMCP(name="AnnualReportAssistant")


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")


# 统一注册所有工具
register_tools(mcp)


custom_middleware = [
    # Bearer 认证中间件
    Middleware(BearerAuthMiddleware),
]


app = create_streamable_http_app(
    server=mcp, streamable_http_path="/mcp", middleware=custom_middleware
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4200)
