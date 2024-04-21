"""The main index page."""

import reflex as rx
from repeat.data import (
    line_chart_data,
    lines,
    pie_chart_data,
    area_chart_data,
    areas,
    stat_card_data,
    tabular_data,
)
from repeat.graphs import (
    area_chart,
    line_chart,
    pie_chart,
    stat_card,
    table,
)
from repeat.template import template

# Content in a grid layout.


def content_grid():
    return (
        rx.chakra.grid(
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Hello, Jerames Zhang 👋", font_size="3rem", font_weight="600"
                    ),
                    rx.image(src="/dashboard/search.svg"),
                    width="100%",
                    display="flex",
                    justify_content="space-between",
                    margin_top="1em",
                    margin_bottom="3em",
                ),
                rx.hstack(
                    rx.image(src="/dashboard/progress.svg"),
                    rx.image(src="/dashboard/goal.svg"),
                    rx.vstack(
                        rx.image(src="/dashboard/grocery_list.svg"),
                        rx.image(src="/dashboard/medical.svg"),
                        height="100%",
                        display="flex",
                        justify_content="space-between",
                    ),
                    width="100%",
                    display="flex",
                    justify_content="space-between",
                    margin_bottom="2em",
                ),
                rx.image(
                    src="/dashboard/recipes.svg", margin_bottom="2em", width="100%"
                ),
                rx.image(
                    src="/dashboard/summary.svg", margin_bottom="2em", width="100%"
                ),
            ),
        ),
    )


@template
def index() -> rx.Component:
    return rx.box(
        rx.box(
            content_grid(),
            margin_top="calc(50px + 2em)",
            padding="3em",
        ),
        padding_x="4em",
    )
