from fastapi import FastAPI
from api import profiles

app = FastAPI(
    title="InterViewMe API",
    description="API для подготовки к собеседованиям с различными типами интервьюеров",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(profiles.router, tags=["Profiles"])