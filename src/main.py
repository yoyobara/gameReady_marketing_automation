from fastapi import FastAPI
import uvicorn

from settings import Settings
from api.new_ad import new_ad_router
from api.webhook import webhook_router

app = FastAPI()
settings = Settings()

app.include_router(new_ad_router, prefix="/new_ad", tags=["new_ad"])
app.include_router(webhook_router, prefix="/webhook", tags=["webhook"])


@app.get("/")
@app.get("/health")
async def health_check() -> str:
    return "ok"


uvicorn.run(app, host=settings.host, port=settings.port)
