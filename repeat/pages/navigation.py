import reflex as rx
from reflex.components import lucide

from repeat.styles import FONT_FAMILY


def sidebar_link(text: str, href: str, icon: str):
    return rx.link(
        rx.flex(
            rx.icon_button(
                rx.icon(tag=icon, weight=16, height=16),
                variant="soft",
            ),
            text,
            py="2",
            px="4",
            spacing="3",
            align="center",
            direction="row",
            font_family=FONT_FAMILY,
        ),
        href=href,
        width="100%",
        border_radius="8px",
        margin_x="2em",  # between each navbar
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
    logo_src = props.get("logo_src", "/logo.jpg")
    heading = props.get("heading", "NOT SET")
    return rx.hstack(
        rx.hstack(  # logo and title
            rx.image(src=logo_src, height="28px", border_radius="8px"),
            rx.heading(
                heading,
                font_family=FONT_FAMILY,
                size="5",
            ),
            width="100%",
            spacing="5",  # between logo and title
            margin="2em",  # entire navbar
        ),
        rx.divider(margin_x="15"),  # space between logo/title and navbar links
        rx.hstack(  # navbar links
            *sidebar_links,
            padding_x="5em",
        ),
        position="fixed",
        height="90px",
        width="100%",
        left="0px",
        top="0px",
        align_items="left",
        z_index="10",
        background_color="rgba(1, 5, 15)",
        # backdrop_filter="blur(10px)",
        # padding="2em", # entire navbar
    )


dashboard_sidebar = sidebar(
    sidebar_link(text="Dashboard", href="/", icon="bar_chart_3"),
    sidebar_link(text="Inventory", href="/inventory", icon="list-todo"),
    sidebar_link(text="Recipes", href="/recipes", icon="cooking-pot"),
    sidebar_link(text="Chat", href="/chat", icon="message-circle"),
    sidebar_link(text="Resources", href="/resources", icon="file-question"),
    logo_src="/logo.jpg",
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
