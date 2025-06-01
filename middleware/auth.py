import os
from collections.abc import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp


class BearerAuthMiddleware(BaseHTTPMiddleware):
    """Bearer Token 认证中间件"""

    def __init__(
        self,
        app: ASGIApp,
        valid_tokens: set[str] = None,
        exclude_paths: set[str] = None,
    ):
        super().__init__(app)
        # 如果没有提供有效 token，使用默认的示例 token
        self.valid_tokens = valid_tokens or [os.getenv("MCP_AUTH_TOKEN")]
        # 排除不需要认证的路径
        self.exclude_paths = exclude_paths or {"/health", "/docs", "/openapi.json"}

    async def dispatch(self, request: Request, call_next: Callable):
        # 检查是否为排除路径
        if request.url.path in self.exclude_paths:
            return await call_next(request)

        # 获取 Authorization header
        authorization = request.headers.get("Authorization")

        if not authorization:
            return JSONResponse(
                status_code=401, content={"error": "Missing Authorization header"}
            )

        # 检查 Bearer token 格式
        if not authorization.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={
                    "error": "Invalid Authorization format. Expected: Bearer <token>"
                },
            )

        # 提取 token
        token = authorization[7:]  # 移除 "Bearer " 前缀

        # 验证 token
        if token not in self.valid_tokens:
            return JSONResponse(
                status_code=401, content={"error": "Invalid or expired token"}
            )

        # 将认证信息添加到请求状态中
        request.state.auth_token = token
        request.state.authenticated = True

        return await call_next(request)
