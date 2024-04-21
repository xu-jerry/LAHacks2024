import reflex as rx
from typing import List, Dict, Any
from repeat.template import template
from gemini.recipes import generate_recipe, substitute_recipe
from gemini.nutrients import nutritional_value, nutrient_evaluation
from gemini.health import health_advice
from ..state.base import State


class FormState(rx.State):
    form_data: dict = {}
    recipe_lines = []
    nutritional_lines = []
    substitute_lines = []
    recipes: List[Dict[str, Any]] = []
    loading = False
    filters = ["high LDL cholesterol levels", "high sodium levels"]

    def build_recipes(self, form_data: dict):
        """Handle the form submit."""

        self.form_data = form_data
        self.loading = True
        yield
        recipes = generate_recipe(
            3, self.form_data["ingredients"], State.user.health_restrictions
        )
        self.recipes = recipes
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

    def substitute_ingredient(self):
        recipe = self.recipes[0]
        # TODO: replace missing with the user input
        self.loading = True
        yield
        substitute_lines = substitute_recipe(
            recipe, "carrots", State.user.inventory_ingredients
        )
        self.substitute_lines = substitute_lines
        print(substitute_lines)
        self.loading = False

    def nutritional_advice(self, nutrient):
        return nutrient_evaluation(nutrient)

    def health_response(self, question):
        return health_advice(question)


@template
def chat() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text("Suggestions based on:"),
                rx.foreach(
                    FormState.filters,
                    lambda filter: rx.box(
                        rx.text(filter),
                        border_radius="8px",
                        background_color="rgba(255,255,255,0.1)",
                        margin_y="0.5em",
                        padding="0.5em 1em",
                    ),
                ),
                margin_top="calc(90px + 4em)",
                padding_right="5em",
                height="500px",
                border_right="0.5px solid rgba(255,255,255,0.3)",
            ),
            rx.box(
                rx.text(
                    "How can I help?",
                    font_size="3em",
                    font_weight="600",
                    margin_bottom="0.5em",
                ),
                rx.hstack(
                    rx.image(src="/chat/goals.svg"),
                    rx.image(
                        src="/chat/nutrition.svg",
                        on_click=FormState.get_nutritional_value,
                    ),
                    rx.image(src="/chat/recipes.svg"),
                    rx.image(src="/chat/health.svg"),
                    width="100%",
                    display="flex",
                    justify_content="space-between",
                ),
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
                            "Time (in hours)",
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
                            recipe["ingredients"].to_string(),
                            color="rgba(255,255,255,0.6)",
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
                        padding="5em",
                        margin_y="2em",  # Add some margin between each recipe card
                        background_color="rgba(50,50,50,0.5)",  # Set background color of recipe card
                        border_radius="12px",  # Add border radius for rounded corners
                        border="1px solid rgba(255,255,255,0.3)",  # Add border to recipe card
                    ),
                ),
                rx.spacer(margin_y="1em"),
                rx.cond(
                    FormState.loading,
                    rx.chakra.circular_progress(is_indeterminate=True),
                    rx.foreach(
                        FormState.recipe_lines, lambda line: rx.box(rx.text(line))
                    ),
                ),
                rx.spacer(margin_y="1em"),
                rx.form(
                    rx.text(
                        "Generate recipes with specific ingredients, tailored to your health conditions.",
                        font_size="0.8em",
                        color="rgba(255,255,255,0.6)",
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="Ingredient(s)",
                            name="ingredients",
                            margin_right="1em",
                            width="60em",
                            padding="1.5em",
                        ),
                        rx.spacer(),  # Adding a spacer to fill the extra space
                        rx.button("Submit", type="submit", padding="1.5em"),
                        width="100%",
                        display="flex",
                        justify_content="space-between",
                        margin_bottom="1em",
                    ),
                    on_submit=FormState.build_recipes,
                    reset_on_submit=True,
                ),
                rx.form(
                    rx.text(
                        "Get nutritional value of a recipe.",
                        font_size="0.8em",
                        color="rgba(255,255,255,0.6)",
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="Recipe",
                            name="recipe",
                            margin_right="1em",
                            width="56em",
                            padding="1.5em",
                        ),
                        rx.spacer(),
                        rx.button(
                            "Nutrional Value",
                            on_click=FormState.get_nutritional_value,
                            padding="1.5em",
                        ),
                        width="100%",
                        display="flex",
                        justify_content="space-between",
                        margin_bottom="1em",
                    ),
                    reset_on_submit=True,
                ),
                rx.form(
                    rx.text(
                        "Substitute an ingredient in a recipe.",
                        font_size="0.8em",
                        color="rgba(255,255,255,0.6)",
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="Ingredient to replace",
                            name="ingredient",
                            margin_right="1em",
                            width="58em",
                            padding="1.5em",
                        ),
                        rx.spacer(),
                        rx.button(
                            "Substitute",
                            on_click=FormState.substitute_ingredient,
                            padding="1.5em",
                        ),
                        width="100%",
                        display="flex",
                        justify_content="space-between",
                        margin_bottom="10em",
                    ),
                    reset_on_submit=True,
                ),
                margin_top="calc(90px + 4em)",
                padding_left="5em",
            ),
            margin_x="7em",
        ),
        # height="calc(100vh - 90px)",
        background_image="url(../chat_gradient.png)",
        background_size="cover",
        background_position="center",
        background_color="rgba(0,0,0)",
    )
