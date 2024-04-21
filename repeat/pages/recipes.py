import reflex as rx
from typing import List, Dict, Any
from repeat.template import template
from gemini.recipes import generate_recipe, substitute_recipe
from gemini.nutrients import nutritional_value, grocery_list_nutrition

filters = ["high protein", "low fat", "no peanuts"]
missing = ["potatoes"]
available = ["carrots"]


class FormState(rx.State):
    form_data: dict = {}
    recipe: List[Dict[str, Any]] = []
    ingredients = ""
    loading = False

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""

        self.form_data = form_data
        self.loading = True
        filter_string = ", ".join(filters)
        yield
        recipe = generate_recipe(2, self.form_data["ingredients"], filter_string)
        self.recipe = recipe
        self.loading = False

    def recipe_info(self):
        """Test recipe_ingredients"""
        self.loading = True
        yield
        self.ingredients = self.recipe["ingredients"]
        self.loading = False

    def sub_rec(self):
        self.loading = True
        yield
        substitute_recipe(self.recipe, missing, available)
        self.loading = False

    def nut_rec(self):
        self.loading = True
        yield
        nutritional_value(self.ingredients)
        self.loading = False

    def groc_list(self):
        ingredients = """
          {
    "ingredient": "Chicken breasts",
    "quantity": 2,
    "unit": ""
  },
  {
    "ingredient": "Potatoes",
    "quantity": 1.5,
    "unit": "pounds"
  },
  {
    "ingredient": "Lemon",
    "quantity": 1,
    "unit": ""
  },
  {
    "ingredient": "Fresh rosemary",
    "quantity": 2,
    "unit": "sprigs"
  },
  {
    "ingredient": "Fresh thyme",
    "quantity": 2,
    "unit": "sprigs"
  },
  {
    "ingredient": "Olive oil",
    "quantity": 2,
    "unit": "tablespoons"
  },
  {
    "ingredient": "Salt",
    "quantity": 1,
    "unit": "teaspoon"
  },
  {
    "ingredient": "Black pepper",
    "quantity": 0.5,
    "unit": "teaspoon"
  }
        """
        self.loading = True
        yield
        grocery_list_nutrition(ingredients)
        self.loading = False


@template
def recipes() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.text("How can I help?", font_size="2.5em"),
                font_weight="600",
                margin_top="calc(50px + 2em)",
                padding_y="2em",
            ),
            rx.foreach(
                FormState.recipe,
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
                        recipe["ingredients"].to_string(), 
                        color="rgba(255,255,255,0.6)"
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
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
            rx.hstack(
                rx.button("Ingredients", on_click=FormState.recipe_info),
                rx.button("Substitute", on_click=FormState.sub_rec),
                rx.button("Nutrition", on_click=FormState.nut_rec),
                rx.button("Grocery List", on_click=FormState.groc_list),
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
