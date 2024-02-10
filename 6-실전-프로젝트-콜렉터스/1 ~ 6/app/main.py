from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models import mongodb
from app.models.book import BookModel




BASE_DIR = Path(__file__).resolve().parent


app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 북북이"}
    )




@app.get("/search", response_class=HTMLResponse)
async def root(request: Request, q: str):
    print(q)
    book = BookModel(keyword="python", publisher='BJPublic', price=1200, image='me.png')
    await mongodb.engine.save(book)
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 북북이", "keyword":q}
    )

@app.on_event("startup")
def on_app_start():
    """before app starts"""
    mongodb.connect()

#
#
@app.on_event("shutdown")
def on_app_shutdown():
    """after app shutdown"""
    # mongodb.close()
