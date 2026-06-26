from fastapi import FastAPI
from uvicorn import Config, Server

from config.config import settings
from src.routes.flights import router as flights_router
from src.routes.templates import router as template_router


def build_app() -> FastAPI:
    app = FastAPI(
        title="Flights AI",
    )

    app.include_router(template_router)
    app.include_router(flights_router)

    return app


def main() -> None:
    config = Config(
        app=build_app(),
        host=settings.host,
        port=settings.port,
    )

    server = Server(config)
    server.run()


if __name__ == '__main__':
    main()
