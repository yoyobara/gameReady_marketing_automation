from jinja2 import Environment, FileSystemLoader

from utils.angles import MarketingAngle


env = Environment(loader=FileSystemLoader("assets/prompts"))
video_prompt_template = env.get_template("video_prompt.jinja2")


def render_video_prompt(angle: MarketingAngle) -> str:
    return video_prompt_template.render(angle=angle)
