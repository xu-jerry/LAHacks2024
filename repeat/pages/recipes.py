import reflex as rx

from repeat.template import template

import google.generativeai as genai
from typing import List, Dict, Any

import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


class FormState(rx.State):
    form_data: dict = {}
    lines = []
    recipes: List[Dict[str, List[str]]] = []

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        self.regenerate()

    def regenerate(self):
        ingredients = self.form_data["ingredients"]
        prompt = (
            f"List out 3 full recipes with {ingredients} as ingredients. Example format:"
            f"**NAME: Mashed Potatoes**"
            f"**Ingredients**"
            f"- 2 pounds Yukon Gold potatoes, peeled and cubed"
            f"- 1/2 cup whole milk"
            f"- 1/4 cup butter, cubed"
            f"- 1/4 cup sour cream"
            f"- Salt and pepper to taste"
            f"**Steps**"
            f"1. Place the potatoes in a large pot of cold water. Bring to a boil and cook until tender, about 15 minutes."
            f"2. Drain the potatoes and return them to the pot. Add the milk, butter, and sour cream."
            f"3. Mash the potatoes with a potato masher or fork until smooth and creamy."
            f"4. Season with salt and pepper to taste."
        )
        response = model.generate_content(prompt)
        self.lines = response.text.split("\n")

        # Parse response to get recipes
        result = []
        current_recipe = {}
        for line in self.lines:
            if line.startswith("**NAME: "):
                # New recipe name
                if current_recipe:
                    result.append(current_recipe)
                current_recipe = {
                    "name": [line.strip("**NAME: ")],
                    "ingredients": [],
                    "steps": [],
                }
            elif line.startswith("**Ingredients**") or line.startswith("**Steps**"):
                # Skip these lines
                pass
            elif line.startswith("-"):
                current_recipe["ingredients"].append(line)
            elif (
                line.startswith("1")
                or line.startswith("2")
                or line.startswith("3")
                or line.startswith("4")
                or line.startswith("5")
                or line.startswith("6")
                or line.startswith("7")
                or line.startswith("8")
                or line.startswith("9")
                or line.startswith("0")
            ):
                current_recipe["steps"].append(line)

        if current_recipe:
            result.append(current_recipe)
        self.recipes = result


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
            # rx.foreach(FormState.lines, lambda line: rx.box(rx.text(line))),
            rx.foreach(  # Use foreach to iterate over recipes
                FormState.recipes,
                lambda recipe: rx.box(  # Each recipe will be displayed in its own box
                    rx.box(
                        rx.foreach(  # Display recipe name
                            recipe["name"],
                            lambda name: rx.text(name, font_weight="800", text_align="center", font_size="2em", margin_bottom="0.8em"),
                        ),
                        rx.divider(),
                        rx.text("Ingredients", margin_top="1em", font_weight="600", font_size="1.5em"),
                        rx.foreach(  # Iterate over ingredients
                            recipe["ingredients"],
                            lambda ingredient: rx.text(ingredient, color="rgba(255,255,255,0.6)"),  # Display each ingredient
                        ),
                        rx.text("Steps", margin_top="1em", font_weight="600", font_size="1.5em"),
                        rx.foreach(  # Iterate over steps
                            recipe["steps"],
                            lambda step: rx.text(step, color="rgba(255,255,255,0.6)"),  # Display each step
                        ),
                        margin_y="2em",  # Add some margin between each recipe card
                        padding="2em",  # Add padding to the recipe card
                        background_color="rgba(50,50,50,0.5)",  # Set background color of recipe card
                        border_radius="12px",  # Add border radius for rounded corners
                        border="1px solid rgba(255,255,255,0.3)",  # Add border to recipe card
                        flex="1",  # Allow each card to grow to occupy equal space
                    )
                ),
                direction="row",  # Arrange recipe cards horizontally
                flex="1",  # Allow the row of cards to grow to occupy available space
                padding="1em",  # Add padding to the row of cards
            ),
            rx.form(
                rx.hstack(  # Use hstack to place elements horizontally
                    rx.input(
                        placeholder="Ingredients",
                        name="ingredients",
                    ),
                    rx.button("Submit", type="submit", margin_left="1em"),
                    width="100%",
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
                padding_bottom="250px",
            ),
            padding_x="250px",
            background_image="url(../chat_gradient.png)",
            background_size="cover",
            background_repeat="no-repeat",
            background_attachment="fixed",
            background_position_y="bottom",
            # height="100vh",
        ),
        # height="calc(100vh - 90px)",
        background_color="rgba(0,0,0,1)",
    )
