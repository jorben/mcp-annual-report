FROM python:3.12-slim

WORKDIR /app

ENV MCP_AUTH_TOKEN

COPY . .

RUN pip install -e .

EXPOSE 4200

CMD ["python", "main.py"]
