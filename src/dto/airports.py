from pydantic import BaseModel


class Flight(BaseModel):
    number: str | None
    airline: str | None
    aircraft: str | None
    origin: str | None
    status: str | None
    time: dict


class AirportData(BaseModel):
    name: str
    flights: list[Flight]
