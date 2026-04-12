import httpx
from json import dumps as jsondumps

HEYGEN_BASE_URL = "https://api.heygen.com/v3"
DEFAULT_AGENT_STYLE_ID = "cb896c823a334e2c8784f8c154007aa8"
DEFAULT_AVATAR_ID = "51c9617998e34ea7b73b118a799c7c65"


class HeyGenClient:
    def __init__(self, api_key):
        self.client = httpx.Client(
            base_url=HEYGEN_BASE_URL, headers={"X-Api-Key": api_key}
        )

    def me(self):
        return self.client.get("/users/me").json()

    def agent_gen(
        self,
        prompt,
        avatar_id=DEFAULT_AVATAR_ID,
    ):
        response = self.client.post(
            "/video-agents",
            json={
                "mode": "generate",
                "prompt": prompt,
                "avatar_id": avatar_id,
                "orientation": "portrait",
            },
        )
        data = response.json()["data"]

        print(jsondumps(data, indent=4))

        return str(data["session_id"])

    def poll_agent(self, session_id):
        response = self.client.get(f"/video-agents/{session_id}")
        data = response.json()["data"]

        print(jsondumps(data, indent=4))

        return data["status"], data["video_id"]

    def poll_video(self, video_id):
        response = self.client.get(f"/videos/{video_id}")
        data = response.json()["data"]

        print(jsondumps(data, indent=4))

        return data["status"], data.get("video_url")
