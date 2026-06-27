from fastapi.templating import Jinja2Templates


async def get_templates() -> Jinja2Templates:
    """
    Constructs a Jinja2Templates instances needed for
    working with templates and returning HTML pages.
    """
    return Jinja2Templates(directory="templates")
