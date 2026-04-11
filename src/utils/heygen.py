from settings import settings
import requests

HEYGEN_BASE_URL = "https://api.heygen.com/v3"


def generate_video_using_agent():
    response = requests.get(
        HEYGEN_BASE_URL + "/users/me",
        headers={"X-Api-Key": settings.heygen_api_key},
    )
    print(response.json())
