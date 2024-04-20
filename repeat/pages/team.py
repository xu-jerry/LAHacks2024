import reflex as rx

from repeat.template import template

@template
def team() -> rx.Component:
    return rx.box(
            rx.box(
                rx.text("placeholder"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        )

