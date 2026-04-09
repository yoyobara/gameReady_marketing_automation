from fastapi import APIRouter

new_ad_router = APIRouter()


@new_ad_router.get("/")
def new_ad() -> dict[str, str]:
    return {"title": "New Ad", "description": "what"}
