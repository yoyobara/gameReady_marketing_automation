from fastapi import APIRouter

webhook_router = APIRouter()


@webhook_router.post("/")
def webhook() -> dict[str, str]:
    return {"result": "webhook_result"}
