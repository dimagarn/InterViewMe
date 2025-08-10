from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from api import profiles

app = FastAPI(
    title="InterViewMe API",
    description="REST API для подготовки к IT-собеседованиям. Получайте типичные фразы, советы по общению и юмористические тактики для разных типов интервьюеров: от технических 'душнил' до расслабленных 'чилл-гаев'",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(profiles.router, tags=["Profiles"])