import reflex as rx

from repeat.template import template
from gemini.recipes import generate_recipe, recipe_ingredients, substitute_recipe

filters = ['high protein', 'low fat', 'no peanuts']

class FormState(rx.State):
    form_data: dict = {}
    lines = []
    loading = False

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        
        self.form_data = form_data
        self.loading= True
        filter_string = ", ".join(filters)
        yield
        recipe = generate_recipe(self.form_data["ingredients"], filter_string)
        self.lines = recipe.split('\n')
        self.loading= False

    def recipe_info(self):
        """Test recipe_ingredients"""
        recipe_ingredients()

    def sub_rec(self):
        substitute_recipe()


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
            rx.button("Ingredients", on_click=FormState.recipe_info),
            rx.button("Substitute", on_click=FormState.sub_rec),
            padding_left="250px",
            padding_right="250px",
        )
