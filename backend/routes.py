import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

#Display html page
templates = Jinja2Templates(directory="templates")

router = fastapi.APIRouter()

@router.get('/index/{param}', include_in_schema=False)
def index(request: Request, param: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": param})