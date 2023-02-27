# type: ignore
"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
import random
import asyncio

TITLE_COLOR = "#E8EAED"
PARAGRAPH_COLOR = "#E8EAED"
ACCENT_COLOR = "#303134"

filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    @pc.var
    def random_bg(self) -> str:
        i=random.randint(1, 6)
        print(f"bg{i}.svg")
        return f"/bgs/bg{random.randint(1, 6)}.svg"

def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Alec Jensen", font_family="Open Sans", font_size="4em", text_align="center", color=TITLE_COLOR),
            pc.spacer(width="20px"),
            pc.icon(tag="minus", color=PARAGRAPH_COLOR),
            pc.spacer(width="20px"),
            pc.text("Frontend Developer | Backend Developer | 3D Artist | Musician | Drone Pilot | ", pc.link(pc.span("Photographer ", pc.icon(tag="external_link")), color="#8AB4F8", href="https://cloud.alecj.tk/s/3fXAebqGMpAYyXe", is_external=True), text_align="center", font_size="22px", font_weight="bold", color=PARAGRAPH_COLOR),
            pc.spacer(width="20px"),
            pc.icon(tag="minus", color=PARAGRAPH_COLOR),
            pc.spacer(width="20px"),
            pc.hstack(
                pc.spacer(),
                pc.link(pc.image(src="/github-mark.svg", height="100%"), href="https://github.com/alec-jensen", is_external=True, color=TITLE_COLOR),
                pc.spacer(),
                pc.link(pc.image(src="/discord.svg", height="100%"), href="https://discord.gg/JjWEVXttFR", is_external=True, color=TITLE_COLOR),
                pc.spacer(),
                pc.link(pc.image(src="/youtube.svg", height="100%"), href="https://www.youtube.com/@alecjensen", is_external=True, color=TITLE_COLOR),
                pc.spacer(),
                height="10%",
                width="30%"
            ),
            pc.spacer(width="20px"),
            pc.icon(tag="minus", color=PARAGRAPH_COLOR),
            pc.spacer(width="20px"),
            pc.text("I'm a 15-year-old who is passionate about technology. I have a lot of experience creating frontends and backends using languages like Python, Java, and C++. When I'm not programming, I enjoy taking pictures, making videos, and playing the viola.",
                    text_align="center", width="80%", font_size="21px", color=PARAGRAPH_COLOR),
            width="70vw",
            padding="20px",
            border_radius="10px",
            backdrop_filter="blur(10px)",
            background_color="rgba(255, 255, 255, 0.05)",
            box_shadow="0px 0px 10px 0px rgba(0,0,0,0.75)",
        ),
        width="100%",
        height="100vh",
        background_image = State.random_bg,
        background_size = "cover",
    )

style = {
    "color": "#2D4263",
    "height": "100%",
    "width": "100%",
}

app = pc.App(state=State, style=style,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap",
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    ],
    description="Alec Jensen's Portfolio",)

app.add_page(index, route="/", title="Alec Jensen", description="Alec Jensen's Portfolio")
app.compile()
