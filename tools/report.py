import os
from typing import Annotated

from fastmcp.exceptions import ToolError
from pydantic import Field


def register_report_tools(mcp):
    """注册所有报告工具到 MCP 实例"""

    @mcp.tool()
    async def list_reports() -> list[str]:
        """Get the list of annual reports."""

        # 获取data目录下的所有文件夹名称，过滤掉.DS_Store文件
        report_list = [f for f in os.listdir("data") if not f.startswith(".")]
        return report_list

    @mcp.tool()
    async def get_report_content(
        report_name: Annotated[
            str,
            Field(description="Name of the report to get content from list_reports"),
        ],
        offset: Annotated[
            int, Field(description="Offset of the report page", ge=0)
        ] = 0,
        limit: Annotated[
            int, Field(description="Limit of the report page", ge=1, le=500)
        ] = 10,
    ) -> dict:
        """Get the report content by name."""

        if report_name not in await list_reports():
            raise ToolError("Report is not found.")
        # 计算目录下md文件数量（按文件名排序）
        md_files = [f for f in os.listdir(f"data/{report_name}") if f.endswith(".md")]
        total_pages = len(md_files)
        md_files.sort()
        # 根据offset和limit计算需要返回的md文件列表
        md_files = md_files[offset : offset + limit]
        # 返回md文件内容
        content = "\n".join(
            [open(f"data/{report_name}/{md_file}").read() for md_file in md_files]
        )
        return {
            "content": content,
            "total_pages": total_pages,
            "current_page_range": f"{offset + 1}-{min(offset + limit, total_pages)}",
        }
