from fastapi import FastAPI
from api import profiles

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(profiles.router)