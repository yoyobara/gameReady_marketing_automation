from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel


class MarketingAngle(BaseModel):
    name: str
    description: str
    target_audience: str
    sample_headline: str
    sample_body: str
    emotional_trigger: str


env = Environment(loader=FileSystemLoader("prompts"))
video_prompt_template = env.get_template("video_prompt.jinja2")


def render_video_prompt(angle: MarketingAngle) -> str:
    return video_prompt_template.render(angle=angle)
