# MCP Annual Report Server

A FastMCP server designed for analyzing annual reports with Bearer Token authentication. This server provides tools to access and process annual report data stored in markdown format.

## 🚀 Features

- **Annual Report Analysis**: Access and analyze annual reports stored as markdown files
- **Bearer Token Authentication**: Secure API access with configurable authentication
- **Paginated Content Access**: Efficient retrieval of large report documents with pagination
- **Health Check Endpoint**: Built-in health monitoring for service availability
- **Modern Python Stack**: Built with FastMCP, Starlette, and other modern Python libraries

## 📁 Project Structure

```
mcp-annual-report/
├── main.py                    # Application entry point
├── pyproject.toml            # Project configuration and dependencies
├── middleware/               # Authentication middleware
│   └── auth.py              # Bearer token authentication
├── tools/                   # MCP tools and functionality
│   ├── __init__.py
│   ├── registry.py          # Tool registration manager
│   └── report.py            # Annual report analysis tools
├── data/                    # Annual report data storage
│   ├── meituan-2019e/       # Sample: Meituan 2019 annual report
│   ├── popmart-2023e/       # Sample: Pop Mart 2023 annual report
│   └── tencent-2024e/       # Sample: Tencent 2024 annual report
├── Makefile                 # Development commands
└── .pre-commit-config.yaml  # Code quality configuration
```

## 🛠️ Installation

### Prerequisites

- Python 3.12 or higher
- uv package manager (recommended) or pip

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jorben/mcp-annual-report.git
   cd mcp-annual-report
   ```

2. **Install dependencies** (using uv):
   ```bash
   make install
   ```

   Or using pip:
   ```bash
   pip install -e .
   ```

3. **Configure environment**:
   Create a `.env` file with your authentication token:
   ```bash
   MCP_AUTH_TOKEN=your_bearer_token_here
   ```

## 🚀 Usage

### Starting the Server

```bash
# using uv
uv run main.py

# or using python
python main.py
```

The server will start on `http://localhost:4200` by default.

### Available Endpoints

- **Health Check**: `GET /health` - No authentication required
- **MCP Interface**: `/mcp` - Requires Bearer token authentication

### Authentication

All API requests (except health check) require Bearer token authentication:

```bash
curl -H "Authorization: Bearer your_token_here" http://localhost:4200/mcp
```

### Available Tools

#### 1. List Reports

Get a list of all available annual reports:

```python
# Tool: list_reports
# Returns: List of report names
```

#### 2. Get Report Content

Retrieve content from a specific annual report with pagination:

```python
# Tool: get_report_content
# Parameters:
#   - report_name: Name of the report (from list_reports)
#   - offset: Starting page number (default: 0)
#   - limit: Number of pages to retrieve (default: 10, max: 500)
# Returns:
#   - content: Concatenated markdown content
#   - total_pages: Total number of pages in the report
#   - current_page_range: Range of pages returned
```

## 🧪 Data Format

Annual reports are stored as individual markdown files in the `data/` directory:

```
data/
└── company-year/
    ├── page_0001.md
    ├── page_0002.md
    └── ...
```

Each markdown file contains the OCR-extracted text content from the corresponding page of the annual report.

## 🔧 Development

### Code Quality Tools

```bash
# Format code
make format

# Lint code
make lint

# Fix linting issues
make fix

# Run pre-commit checks
make check
```

### Adding New Reports

1. Create a new directory under `data/` with the format `company-year`
2. Add markdown files with the naming pattern `page_XXXX.md`
3. Ensure files are numbered sequentially for proper pagination

## 📦 Dependencies

### Core Dependencies

- **fastmcp**: FastMCP framework for building MCP servers
- **python-dotenv**: Environment variable management
- **starlette**: ASGI framework for web applications
- **uvicorn**: ASGI server implementation

### Development Dependencies

- **pre-commit**: Git hook framework for code quality
- **ruff**: Fast Python linter and formatter

## 🔐 Security

- Bearer token authentication for API access
- Configurable token validation
- Path-based exclusions for public endpoints
- Request state management for authenticated requests

## 📝 License

This project is licensed under the terms specified in the LICENSE file.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the code quality checks: `make check`
5. Submit a pull request

## 📞 Support

For issues and questions, please use the GitHub issue tracker.
