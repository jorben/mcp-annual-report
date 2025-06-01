FROM python:3.12-slim

WORKDIR /app

# 安装locales包并设置UTF-8环境
RUN apt-get update && \
    apt-get install -y locales && \
    rm -rf /var/lib/apt/lists/* && \
    sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen

# 设置环境变量确保 UTF-8 编码
ENV MCP_AUTH_TOKEN=pls-change-me
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV PYTHONIOENCODING=utf-8
ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install -e .

EXPOSE 4200

CMD ["python", "main.py"]
