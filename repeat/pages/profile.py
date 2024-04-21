import reflex as rx
from repeat.template import template

def content_grid():
    return (
        rx.chakra.grid(
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Profile", font_size="3rem", font_weight="600"
                    ),
                    rx.image(src="/dashboard/search.svg"),
                    width="100%",
                    margin_bottom="3em",
                ),
                rx.hstack(
                    rx.vstack(
                        rx.image(src="/profile/your-info.svg", margin_bottom="1em"),
                        rx.image(src="/profile/your-records.svg"),
                    ),
                    rx.vstack(
                        rx.image(src="/dashboard/goal.svg", margin_bottom="1em"),
                        rx.image(src="/profile/grocery-list.svg"),
                        margin_x="1em",
                    ),
                    rx.vstack(
                        rx.image(src="/profile/medical-info.svg"),
                    ),
                    width="100%",
                ),
            ),
        ),
    )


@template
def profile() -> rx.Component:
    return rx.box(
        rx.box(
            content_grid(),
            margin_top="calc(50px + 2em)",
            padding="3em",
        ),
        padding_x="4em",
    )
