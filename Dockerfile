FROM ghcr.io/astral-sh/uv:python3.14-alpine
COPY . /app
WORKDIR /app
RUN ["uv", "sync"]
ENTRYPOINT ["uv", "run", "flask", "run", "-h", "0.0.0.0"]
