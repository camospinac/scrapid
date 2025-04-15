from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="scrapid", version="0.1.0")

app.include_router(api_router)