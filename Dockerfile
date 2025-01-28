FROM python:3.12.6-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY . .
RUN uv sync --frozen
# TODO: Non-urgently, switch to waitress or similar
# TODO: fix user
CMD ["uv", "run", "fastapi", "run", "epic_fail/main.py"]
