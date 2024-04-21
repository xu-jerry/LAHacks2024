import reflex as rx
from repeat.template import template

@template
def example_recipe() -> rx.Component:
    return rx.box(
        rx.image(src="/recipes/baked_potato_recipe.svg", width="120em"),
        padding_top="90px",
    )