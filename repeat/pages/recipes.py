import reflex as rx
from repeat.template import template

@template
def recipes() -> rx.Component:
    return rx.box(
            rx.vstack(
              rx.box(
                rx.text("Recipes",font_size="2em",),
                margin_top="calc(50px + 2em)",
                padding_left="1em",
                padding_bottom="1em",
                font_size="35px",
              ),
              rx.box(
                rx.text("Suggested", font_weight="bold", margin_bottom="10px"),
                rx.hstack(
                    rx.link(
                        rx.image(src="/recipes/baked_potato.svg", width="25em"),
                        href="/baked_potato_recipe",
                      ),
                    rx.link(
                      rx.image(src="/recipes/chicken_lentil_soup.svg", width="25em"),
                      href="/baked_potato_recipe",
                    ),
                    rx.link(
                      rx.image(src="/recipes/flatbreads_with_zaatar.svg", width="25em"),
                      href="/baked_potato_recipe",
                    ),
                ),
                margin_top="calc(5px)",
                padding_left="2em",
              ),
              rx.box(
                rx.text("All", font_weight="bold", margin_bottom="10px"),
                rx.image(src="/recipes/filter.svg", width="75em", margin_bottom="10px"),
                rx.hstack(
                    rx.link(
                        rx.image(src="/recipes/sushi.svg", width="25em"),
                        href="/baked_potato_recipe",
                      ),
                      rx.link(
                        rx.image(src="/recipes/bento_box.svg", width="25em"),
                        href="/baked_potato_recipe",
                      ),
                      rx.link(
                        rx.image(src="/recipes/new_york_bagel.svg", width="25em"),
                        href="/baked_potato_recipe",
                      ),
                ),
                margin_top="calc(50px + 2em)",
                margin_bottom="10px",
                padding="2em",
              ),
            ),
            padding_left="250px",
            color="rgb(255, 255, 255, 1)"
    )
