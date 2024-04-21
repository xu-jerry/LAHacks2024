import reflex as rx
from repeat.template import template

@template
def resources() -> rx.Component:
    return rx.box(
        rx.image(src="/resources.svg", width="120em"),
        padding_top="90px",
    )