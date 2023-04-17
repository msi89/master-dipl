from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from router import default as default_api
import uvicorn

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")

templates = Jinja2Templates(directory="templates",
                            autoescape=False, auto_reload=True)

app.include_router(prefix="", router=default_api.router)


@app.get('/health')
def health_check():
    return {"message": "service is running"}


@app.get("/", include_in_schema=False)
def home_page(request: Request, response_class=HTMLResponse, ):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
