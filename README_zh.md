<div align="center">
<h1>年报MCP服务</h1>
<p align="center"><a href="./README.md">English</a> | 简体中文</p>
</div>

一个专为年报分析设计的 FastMCP 服务器，具备 Bearer Token 身份验证功能。该服务器提供工具来访问和处理以 Markdown 格式存储的年报数据。

## 🚀 功能特性

- **年报分析**：访问和分析以 Markdown 文件存储的年报数据
- **Bearer Token 身份验证**：具有可配置身份验证的安全 API 访问
- **分页内容访问**：高效检索大型报告文档，支持分页功能
- **健康检查端点**：内置健康监控以确保服务可用性
- **现代 Python 技术栈**：基于 FastMCP、Starlette 和其他现代 Python 库构建

## 📁 项目结构

```
mcp-annual-report/
├── main.py                    # 应用程序入口点
├── pyproject.toml            # 项目配置和依赖项
├── middleware/               # 身份验证中间件
│   └── auth.py              # Bearer token 身份验证
├── tools/                   # MCP 工具和功能
│   ├── __init__.py
│   ├── registry.py          # 工具注册管理器
│   └── report.py            # 年报分析工具
├── data/                    # 年报数据存储
│   └── popmart-2023e/       # 示例：泡泡玛特 2023 年报
├── Makefile                 # 开发命令
└── .pre-commit-config.yaml  # 代码质量配置
```

## 🛠️ 安装

### 前置要求

- Python 3.12 或更高版本
- uv 包管理器（推荐）或 pip

### 设置步骤

1. **克隆仓库**：
   ```bash
   git clone https://github.com/jorben/mcp-annual-report.git
   cd mcp-annual-report
   ```

2. **安装依赖**（使用 uv）：
   ```bash
   make install
   ```

   或使用 pip：
   ```bash
   pip install -e .
   ```

3. **配置环境变量**：
   创建 `.env` 文件并设置您的身份验证令牌：
   ```bash
   MCP_AUTH_TOKEN=your_bearer_token_here
   ```

## 🚀 使用方法

### 启动服务器


```bash
uv run main.py
# 或
python main.py
```

服务器将默认在 `http://localhost:4200` 上启动。

### 可用端点

- **健康检查**：`GET /health` - 无需身份验证
- **MCP 接口**：`/mcp` - 需要 Bearer token 身份验证

### 身份验证

所有 API 请求（健康检查除外）都需要 Bearer token 身份验证：

```bash
curl -H "Authorization: Bearer your_token_here" http://localhost:4200/mcp
```

### 可用工具

#### 1. 列出报告

获取所有可用年报的列表：

```python
# 工具：list_reports
# 返回：报告名称列表
```

#### 2. 获取报告内容

从特定年报中检索内容，支持分页：

```python
# 工具：get_report_content
# 参数：
#   - report_name: 报告名称（来自 list_reports）
#   - offset: 起始页码（默认：0）
#   - limit: 要检索的页数（默认：10，最大：500）
# 返回：
#   - content: 连接的 Markdown 内容
#   - total_pages: 报告总页数
#   - current_page_range: 返回的页面范围
```

## 🧪 数据格式

年报以单独的 Markdown 文件形式存储在 `data/` 目录中：

```
data/
└── company-year/
    ├── page_0001.md
    ├── page_0002.md
    └── ...
```

每个 Markdown 文件包含从年报相应页面提取的 OCR 文本内容。

## 🔧 开发

### 代码质量工具

```bash
# 格式化代码
make format

# 代码检查
make lint

# 修复代码检查问题
make fix

# 运行预提交检查
make check
```

### 添加新报告

1. 在 `data/` 下创建新目录，格式为 `company-year`
2. 添加遵循命名模式 `page_XXXX.md` 的 Markdown 文件
3. 确保文件按顺序编号以便正确分页

## 📦 依赖项

### 核心依赖

- **fastmcp**：构建 MCP 服务器的 FastMCP 框架
- **python-dotenv**：环境变量管理
- **starlette**：用于 Web 应用程序的 ASGI 框架
- **uvicorn**：ASGI 服务器实现

### 开发依赖

- **pre-commit**：代码质量的 Git 钩子框架
- **ruff**：快速的 Python 代码检查器和格式化工具

## 🔐 安全性

- 用于 API 访问的 Bearer token 身份验证
- 可配置的令牌验证
- 公共端点的基于路径的排除
- 经过身份验证的请求的请求状态管理

## 📝 许可证

该项目根据 LICENSE 文件中指定的条款获得许可。

## 🤝 贡献

1. Fork 仓库
2. 创建功能分支
3. 进行更改
4. 运行代码质量检查：`make check`
5. 提交拉取请求

## 📞 支持

如有问题和疑问，请使用 GitHub 问题跟踪器。

## 🎯 技术架构

### MCP 协议集成

该项目基于 Model Context Protocol (MCP) 构建，这是一个标准化的协议，用于在语言模型和外部工具之间进行通信。

### 中间件架构

- **认证中间件**：实现 Bearer token 验证，确保 API 安全
- **可扩展设计**：易于添加新的中间件功能

### 工具管理

- **模块化工具注册**：通过 `tools/registry.py` 统一管理所有工具
- **分离关注点**：每个工具模块专注于特定功能领域

## 📊 使用场景

### 金融分析

- 快速访问和分析上市公司年报
- 支持多家公司的数据对比分析
- 提供结构化的数据访问接口

### 研究应用

- 学术研究中的企业数据获取
- 投资决策支持系统
- 自动化报告生成

### 集成应用

- 与 AI 模型结合进行智能分析
- 作为更大系统中的数据源组件
- 支持批量数据处理和分析

## 🔧 高级配置

### 环境变量

```bash
# 必需配置
MCP_AUTH_TOKEN=your_bearer_token_here

# 可选配置
MCP_HOST=0.0.0.0          # 服务器主机地址
MCP_PORT=4200             # 服务器端口
MCP_DEBUG=false           # 调试模式
```

### 自定义认证

您可以通过修改 `middleware/auth.py` 来实现自定义认证逻辑：

```python
# 支持多个有效令牌
valid_tokens = {"token1", "token2", "token3"}

# 自定义排除路径
exclude_paths = {"/health", "/docs", "/custom-endpoint"}
```

## 🚀 性能优化

### 分页策略

- 默认每页 10 个文档，最大支持 500 个
- 智能缓存机制减少磁盘 I/O
- 支持并发请求处理

### 内存管理

- 按需加载文档内容
- 自动垃圾回收未使用的数据
- 优化的文件读取策略

## 🔍 故障排除

### 常见问题

1. **认证失败**：检查 `.env` 文件中的 `MCP_AUTH_TOKEN` 设置
2. **端口冲突**：确保端口 4200 未被其他服务占用
3. **文件权限**：确保 `data/` 目录具有适当的读取权限

### 日志和调试

启用调试模式以获取详细的日志信息：

```bash
export MCP_DEBUG=true
python main.py
```
