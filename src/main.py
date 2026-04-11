from api.heygen import HeyGenClient
from settings import settings
import json


def ad_gen(request):
    pass


def test():
    client = HeyGenClient(settings.heygen_api_key)
    json.dump(
        client.client.get("/video-agents/styles").json(), open("styles.json", "w")
    )


if __name__ == "__main__":
    test()
