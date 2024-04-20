import reflex as rx
from reflex.components import lucide

from repeat.styles import FONT_FAMILY


def sidebar_link(text: str, href: str):
    return rx.link(
        rx.flex(
            text,
            spacing="3",
            align="center",
            direction="row",
            font_family=FONT_FAMILY,
            color="rgba(255, 255, 255, 1)",
            font_weight="600",
        ),
        href=href,
        border_radius="8px",
        margin_x="1em",  # Reduce margin between each navbar link
        margin_y="1em",
        padding="1em",
        _hover={
            "background": "rgba(255, 255, 255, 0.1)",
            "backdrop_filter": "blur(10px)",
        },
    )


def sidebar(
    *sidebar_links,
    **props,
) -> rx.Component:
    logo_src = props.get("logo_src", "/logo.png")
    heading = props.get("heading", "NOT SET")
    return rx.vstack(
        rx.hstack(
            rx.hstack(  # logo and title
                rx.image(
                    src=logo_src, height="28px", border_radius="8px", margin_left="2em"
                ),
                rx.heading(
                    heading,
                    font_family=FONT_FAMILY,
                    size="5",
                ),
                spacing="3",  # between logo and title
                margin="2em",  # entire navbar
            ),
            rx.hstack(  # navbar links
                *sidebar_links,
                padding_x="2em",  # Reduce padding between navbar links
                margin_left="10em",
            ),
            position="fixed",
            height="90px",
            top="0px",
            align_items="center",
            z_index="10",
            background_color="rgba(1, 5, 15)",
            # backdrop_filter="blur(10px)",
            # padding="2em", # entire navbar
        ),
        rx.box(  # Line under navbar with white in the center and fades to black on ends
            height="1px",
            background_image="linear-gradient(to right, rgba(0,0,0,1), rgba(255,255,255,0.5), rgba(0,0,0,1))",
            width="100vw",
            position="fixed",
            top="90px",
            z_index="10",  # Ensure it's above other content
        ),
    )


dashboard_sidebar = sidebar(
    sidebar_link(text="Dashboard", href="/"),
    sidebar_link(text="Inventory", href="/inventory"),
    sidebar_link(text="Recipes", href="/recipes"),
    sidebar_link(text="Chat with Cheffy", href="/chat"),
    sidebar_link(text="Resources", href="/resources"),
    logo_src="/logo.png",
    heading="RepEat",
)


# def navbar(heading: str) -> rx.Component:
#     return rx.hstack(
#         rx.heading(heading, font_family=FONT_FAMILY, size="7"),
#         rx.spacer(),
#         rx.menu.root(
#             rx.menu.trigger(
#                 rx.button(
#                     "Menu",
#                     lucide.icon(tag="chevron_down", weight=16, height=16),
#                     font_family=FONT_FAMILY,
#                     variant="soft",
#                 ),
#             ),
#             rx.menu.content(
#                 rx.menu.item("Settings"),
#                 rx.menu.item("Profile"),
#                 rx.menu.item("Logout"),
#                 font_family=FONT_FAMILY,
#                 variant="soft",
#             ),
#             variant="soft",
#             font_family=FONT_FAMILY,
#         ),
#         position="fixed",
#         width="calc(100% - 250px)",
#         top="0px",
#         z_index="1000",
#         padding_x="2em",
#         padding_top="2em",
#         padding_bottom="1em",
#         backdrop_filter="blur(10px)",
#     )
