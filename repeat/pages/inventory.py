import reflex as rx

from repeat.template import template

@template
def inventory() -> rx.Component:
    return rx.box(
            rx.box(
                rx.text("Inventory", color="rgba(0, 0, 0, 0)",),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            rx.box(
                rx.text("Appliances"),
                margin_top="calc(50px + 2em)",
                padding="2em",
                # color="rgba(0, 0, 0, 0)",
            ),
            padding_left="250px",
        )

