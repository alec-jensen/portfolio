# type: ignore
"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
import random
import asyncio

TITLE_COLOR = "#E8EAED"
PARAGRAPH_COLOR = "#B6BABF"
ACCENT_COLOR = "#303134"
DIVIDER_COLOR = "#3C4043"

filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    pass

def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Alec Jensen", font_family="Open Sans", font_size="100px", color=TITLE_COLOR),
            pc.spacer(width="20px"),
            pc.divider(border_color=DIVIDER_COLOR),
            pc.spacer(width="20px"),
            pc.text("Frontend Developer | Backend Developer | 3D Artist | Musician | Drone Pilot | ", pc.link("Photographer", color="#8AB4F8", href="https://cloud.alecj.tk/s/3fXAebqGMpAYyXe", is_external=True), font_size="20px", color=PARAGRAPH_COLOR),
            pc.spacer(width="20px"),
            pc.divider(border_color=DIVIDER_COLOR),
            pc.spacer(width="20px"),
            pc.hstack(
                pc.link(pc.image(src="/github-mark.svg", height="60px"), href="https://github.com/alec-jensen", is_external=True, color=TITLE_COLOR),
                pc.spacer(),
                pc.link(pc.image(src="/discord.svg", height="70px"), href="https://discord.gg/JjWEVXttFR", is_external=True, color=TITLE_COLOR),
                pc.spacer(),
                pc.link(pc.image(src="/youtube.svg", height="70px"), href="https://www.youtube.com/@alecjensen", is_external=True, color=TITLE_COLOR),
                height="70px",
                width="30%"
            ),
            pc.spacer(width="20px"),
            pc.divider(border_color=DIVIDER_COLOR),
            pc.spacer(width="20px"),
            pc.text("I'm a 15-year-old who is passionate about programming. I have a lot of experience creating frontends and backends using languages like Python, Java, and C++. When I'm not programming, I enjoy taking pictures, making videos, and playing the viola.", text_align="center", width="50%", font_size="20px", color=PARAGRAPH_COLOR),
            width="80%",
        )
    )

style = {
    "color": "#2D4263",
    "background_color": "#202124",
}

app = pc.App(state=State, style=style,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap",
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    ])

app.add_page(index, route="/", title="Alec Jensen")
app.compile()
