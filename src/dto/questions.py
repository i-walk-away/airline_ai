from pydantic import BaseModel


class QuestionDTO(BaseModel):
    question: str
    airport: str


class AnswerResponseDTO(BaseModel):
    answer: str
