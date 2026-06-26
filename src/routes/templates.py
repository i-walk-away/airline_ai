from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.core.dependencies.templates import get_templates

router = APIRouter(
    tags=["templates"]
)


@router.get("/", response_class=HTMLResponse)
async def home(
        request: Request,
        templates: Jinja2Templates = Depends(get_templates)
) -> HTMLResponse:
    return templates.TemplateResponse(request, "main.html")
