import reflex as rx
from typing import List, Dict, Any
import json
from repeat.template import template
from gemini.recipes import generate_recipe, substitute_recipe
from gemini.nutrients import nutritional_value
from gemini.health import evaluate_health, create_plan, health_advice
from ..state.base import State

class FormState(rx.State):
    form_data: dict = {}
    recipe_lines = []
    nutritional_lines = []
    recipes: List[Dict[str, Any]] = []
    loading = False
    filters = ["high LDL cholesterol levels", "high sodium levels"]

    def build_recipes(self, form_data: dict):
        """Handle the form submit."""

        self.form_data = form_data
        self.loading = True
        yield
        recipes = generate_recipe(3, self.form_data["ingredients"], State.user.health_restrictions)
        self.recipes = recipes
        print(recipes)
        self.loading = False

    def get_nutritional_value(self):
        recipe = self.recipes[0]
        ingredients = str(recipe["ingredients"])
        self.loading = True
        yield
        nutritional_lines = nutritional_value(ingredients)
        self.nutritional_lines = nutritional_lines
        print(nutritional_lines)
        self.loading = False


@template
def chat() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.text("How can I help?", font_size="2.5em"),
                font_weight="600",
                margin_top="calc(50px + 2em)",
                padding_y="2em",
            ),
            rx.text("Using the following filters:"),
            rx.foreach(FormState.filters, lambda filter: rx.box(rx.text(filter))),
            rx.cond(
                FormState.loading,
                rx.chakra.circular_progress(is_indeterminate=True),
                rx.foreach(FormState.recipe_lines, lambda line: rx.box(rx.text(line))),
            ),
            rx.spacer(margin_y="50px"),
            rx.foreach(
                FormState.recipes,
                lambda recipe: rx.box(
                    rx.text(
                        recipe["name"],
                        font_weight="800",
                        text_align="center",
                        font_size="2em",
                        margin_bottom="0.8em",
                    ),
                    rx.divider(),
                    rx.text(
                        "Time",
                        margin_top="1em",
                        font_weight="600",
                        font_size="1.5em",
                    ),
                    rx.text(recipe["time"], color="rgba(255,255,255,0.6)"),
                    rx.text(
                        "Ingredients",
                        margin_top="1em",
                        font_weight="600",
                        font_size="1.5em",
                    ),
                    # Extracting only ingredient names from the recipe
                    rx.text(
                        recipe["ingredients"].to_string(), color="rgba(255,255,255,0.6)"
                    ),
                    rx.text(
                        "Instructions",
                        margin_top="1em",
                        font_weight="600",
                        font_size="1.5em",
                    ),
                    rx.text(
                        recipe["instructions"].to_string(),
                        color="rgba(255,255,255,0.6)",
                    ),
                    direction="row",  # Arrange recipe cards horizontally
                    flex="1",  # Allow the row of cards to grow to occupy available space
                    padding="3em",  # Add padding to the row of cards
                    margin_y="2em",  # Add some margin between each recipe card
                    background_color="rgba(50,50,50,0.5)",  # Set background color of recipe card
                    border_radius="12px",  # Add border radius for rounded corners
                    border="1px solid rgba(255,255,255,0.3)",  # Add border to recipe card
                ),
            ),
            rx.form(
                rx.hstack(
                    rx.input(
                        placeholder="Ingredients",
                        name="ingredients",
                    ),
                    rx.button("Submit", type="submit"),
                ),
                on_submit=FormState.build_recipes,
                reset_on_submit=True,
            ),
            rx.hstack(
                rx.button("Nutrional Value", on_click=FormState.get_nutritional_value),
                padding_left="250px",
                margin_y="5em",
            ),
            padding_x="250px",
            background_image="url(../chat_gradient.png)",
            background_size="cover",
            background_position="center",
            # height="100vh",
        ),
        # height="calc(100vh - 90px)",
        background_color="rgba(0,0,0)",
    )