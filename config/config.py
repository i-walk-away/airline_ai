from dotenv import find_dotenv, load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv(".env"))


class OpenRouter(BaseSettings):
    api_key: str = Field(alias="OPENROUTER_API_KEY")


class FlightApi(BaseSettings):
    api_key: str = Field(alias="FLIGHT_API_KEY")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    host: str = Field(default="127.0.0.1", alias="APP_HOST")
    port: int = Field(default=8080, alias="APP_PORT")

    flight_api: FlightApi = Field(default_factory=FlightApi)
    open_router: OpenRouter = Field(default_factory=OpenRouter)


settings = Settings()
