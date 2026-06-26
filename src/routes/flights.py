# pylint: disable=missing-function-docstring
from fastapi import APIRouter
from fastapi.params import Depends

from src.core.dependencies.services.flights import get_flights_service
from src.dto.questions import AnswerResponseDTO, QuestionDTO
from src.services.flights import FlightsService

router = APIRouter(
    tags=["flights"]
)


@router.post(
    "/ask",
    description="Ask a question about given flight to LLM.",
    response_model=AnswerResponseDTO
)
async def ask_about_flight(
        data: QuestionDTO,
        flights_service: FlightsService = Depends(get_flights_service)
) -> AnswerResponseDTO:
    answer = await flights_service.ask_about_flight(data)
    return AnswerResponseDTO(answer=answer)
