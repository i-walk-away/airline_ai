FROM python:3.14.2

COPY --from=ghcr.io/astral-sh/uv:0.9.26 /uv /uvx /bin/
WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --locked

COPY . .

EXPOSE $APP_PORT
CMD ["uv", "run", "python", "main.py"]