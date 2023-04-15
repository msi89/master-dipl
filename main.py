from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from router import default as default_api


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")
templates = Jinja2Templates(directory="templates",
                            autoescape=False, auto_reload=True)

app.include_router(prefix="", router=default_api.router)


@app.get("/")
def home_page(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse("index.html", {"request": request})
