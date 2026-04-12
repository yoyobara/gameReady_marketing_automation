from time import sleep

from api.heygen import HeyGenClient
from settings import settings
from utils.angles import get_random_marketing_angle
from utils.prompts import render_video_prompt


def ad_gen(request):
    client = HeyGenClient(settings.heygen_api_key)
    prompt = render_video_prompt(get_random_marketing_angle())
    session_id = client.agent_gen(prompt)

    status, video_id = client.poll_agent(session_id)
    while status != "completed":
        sleep(1)
        status, video_id = client.poll_agent(session_id)

    status, video_url = client.poll_video(video_id)
    assert status == "completed"

    print(video_url)


def test():
    ad_gen(None)


if __name__ == "__main__":
    test()
