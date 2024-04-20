"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from LAHacks2024.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from LAHacks2024.pages.recipes import recipes
from LAHacks2024.pages.team import team
from LAHacks2024.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(recipes, route="/recipes")
app.add_page(team, route="/team")
