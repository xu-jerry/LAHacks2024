"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from repeat.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from .state.base import State
from repeat.pages.login import login
from repeat.pages.signup import signup
from repeat.pages.recipes import recipes
from repeat.pages.inventory import inventory
from repeat.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/", on_load=State.check_login())
app.add_page(login, route="/login")
app.add_page(signup, route="/signup")
app.add_page(recipes, route="/recipes")
app.add_page(inventory, route="/inventory")
