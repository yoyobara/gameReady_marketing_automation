from time import sleep
import logging
import sys

from api.heygen import HeyGenClient
from settings import settings
from utils.assets import get_random_marketing_angle, load_agent_assets
from utils.prompts import render_video_prompt

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log", "a"), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)


def ad_gen(request):
    client = HeyGenClient(settings.heygen_api_key)
    prompt = render_video_prompt(get_random_marketing_angle())

    session_id = client.agent_gen(prompt, load_agent_assets().values())

    while True:
        status, video_id = client.poll_agent(session_id)

        if status == "completed":
            break

        sleep(30)

    status, video_url = client.poll_video(video_id)
    assert status == "completed"

    print(video_url)


def test():
    ad_gen(None)


if __name__ == "__main__":
    test()
