from pydantic import BaseModel
import json
import random
from functools import lru_cache


class MarketingAngle(BaseModel):
    name: str
    description: str
    target_audience: str
    sample_headline: str
    sample_body: str
    emotional_trigger: str


@lru_cache(maxsize=1)
def load_marketing_angles() -> list[MarketingAngle]:
    with open("assets/marketing_angles.json", "r") as f:
        angles_json = json.load(f)
    return [MarketingAngle(**angle) for angle in angles_json]


@lru_cache(maxsize=1)
def load_agent_assets() -> dict[str, str]:
    with open("assets/agent_assets.json", "r") as f:
        return json.load(f)


def get_random_marketing_angle() -> MarketingAngle:
    return random.choice(load_marketing_angles())
