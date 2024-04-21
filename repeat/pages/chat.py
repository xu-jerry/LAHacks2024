import reflex as rx
from repeat.template import template

@template
def chat() -> rx.Component:
    return rx.box(
            rx.box(
                rx.text("Chat"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        )