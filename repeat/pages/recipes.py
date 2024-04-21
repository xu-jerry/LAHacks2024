import reflex as rx
from repeat.template import template


@template
def recipes() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("Recipes", font_size="3rem", font_weight="600"),
            rx.image(src="/dashboard/search.svg"),
            width="100%",
            display="flex",
            justify_content="space-between",
            align_items="center",
            margin_top="calc(90px + 4em)",
        ),
        rx.box(
            rx.text("Suggested", font_weight="bold", margin_bottom="2em"),
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/recipes/baked_potato.svg",
                    ),
                    href="/baked_potato_recipe",
                ),
                rx.link(
                    rx.image(
                        src="/recipes/chicken_lentil_soup.svg",
                    ),
                    href="/baked_potato_recipe",
                ),
                rx.link(
                    rx.image(
                        src="/recipes/flatbreads_with_zaatar.svg",
                    ),
                    href="/baked_potato_recipe",
                ),
                width="100%",
                display="flex",
                justify_content="space-between",
            ),
            margin_top="2em",
        ),
        rx.box(
            rx.text("All", font_weight="bold", margin_bottom="1em"),
            rx.image(src="/recipes/filter.svg", width="100%", margin_bottom="2em"),
            rx.hstack(
                rx.link(
                    rx.image(src="/recipes/sushi.svg"),
                    href="/baked_potato_recipe",
                ),
                rx.link(
                    rx.image(src="/recipes/bento_box.svg"),
                    href="/baked_potato_recipe",
                ),
                rx.link(
                    rx.image(src="/recipes/new_york_bagel.svg"),
                    href="/baked_potato_recipe",
                ),
                width="100%",
                display="flex",
                justify_content="space-between",
            ),
            margin_top="3em",
            margin_bottom="5em",
        ),
        margin_x="7em",
        color="rgb(255, 255, 255, 1)",
    )
