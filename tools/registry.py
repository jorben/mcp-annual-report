"""
工具注册管理器
统一管理所有工具模块的注册
"""

from .report import register_report_tools


def register_tools(mcp):
    """
    统一注册所有工具到 MCP 实例

    这个函数会自动调用所有工具模块的注册函数，
    实现工具的统一管理，但保持各个工具模块的分离
    """

    # 注册报告工具
    register_report_tools(mcp)
