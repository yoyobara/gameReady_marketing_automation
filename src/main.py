from api.heygen import HeyGenClient
from settings import settings


def ad_gen(request):
    pass


def test():
    client = HeyGenClient(settings.heygen_api_key)
    print(client.me())


if __name__ == "__main__":
    test()
