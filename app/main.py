from fastapi import FastAPI
from app.health import router as health_router

app = FastAPI(title="Simple FastAPI CI/CD")

app.include_router(health_router)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}
