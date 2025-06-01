FROM python:3.12-slim

WORKDIR /app

ENV MCP_AUTH_TOKEN=pls-change-me
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONIOENCODING=utf-8

COPY . .

RUN pip install -e .

EXPOSE 4200

CMD ["python", "main.py"]
