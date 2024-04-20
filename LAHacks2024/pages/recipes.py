import reflex as rx

from LAHacks2024.template import template

import google.generativeai as genai

import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


class FormState(rx.State):
    form_data: dict = {}
    lines = []

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        self.regenerate()

    def regenerate(self):
        ingredients = self.form_data["ingredients"]
        prompt = f"List out some full recipes with {ingredients} as ingredients."
        response = model.generate_content(prompt)
        self.lines = response.text.split("\n")


@template
def recipes() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.text("Recipes"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            rx.foreach(FormState.lines, lambda line: rx.box(rx.text(line))),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Ingredients",
                        name="ingredients",
                    ),
                    rx.button("Submit", type="submit"),
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
            padding_left="250px",
            background_image="url(../chat_gradient.png)",
            background_size="cover",
            background_position="center",
            height="100vh",
        ),
        # height="calc(100vh - 90px)",
        background_color="rgba(0,0,0)",
    )
