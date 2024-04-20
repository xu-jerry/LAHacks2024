import os
from dotenv import load_dotenv

import reflex as rx
import google.generativeai as genai
from repeat.template import template

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

filters = ['high protein', 'low fat', 'no peanuts']

class FormState(rx.State):
    form_data: dict = {}
    lines = []
    loading = False

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        
        self.form_data = form_data
        self.loading= True
        yield
        self.regenerate()
  
    def regenerate(self):
        ingredients = self.form_data["ingredients"]
        filter_string = ", ".join(filters)
        prompt = f"List out some full recipes with {ingredients} as ingredients. Please make sure each recipe is {filter_string}. Append the Nutrition Information after each recipe, and the additional ingredients each requires."
        response = model.generate_content(prompt)
        self.lines = response.text.split('\n')
        self.loading= False

@template
def recipes() -> rx.Component:
    return rx.box(
            rx.box(
                rx.text("Recipes"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            rx.text("Using the following filters:"),
            rx.foreach(filters, lambda filter: rx.box(
                        rx.text(filter))),
            rx.cond(
                    FormState.loading,
                    rx.chakra.circular_progress(is_indeterminate=True),
                    rx.foreach(FormState.lines, lambda line: rx.box(
                        rx.text(line)))
                    ),
            rx.divider(),
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
            padding_right="250px",
        )
