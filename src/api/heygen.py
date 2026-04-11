import httpx

HEYGEN_BASE_URL = "https://api.heygen.com/v3"
DEFAULT_AGENT_STYLE_ID = "cb896c823a334e2c8784f8c154007aa8"


class HeyGenClient:
    def __init__(self, api_key: str) -> None:
        self.client = httpx.Client(
            base_url=HEYGEN_BASE_URL, headers={"X-Api-Key": api_key}
        )

    def me(self):
        return self.client.get("/users/me").json()

    def gen_agent(style_id: str = DEFAULT_AGENT_STYLE_ID):
        pass
