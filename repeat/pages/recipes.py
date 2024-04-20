import reflex as rx

from repeat.template import template
from gemini.recipes import generate_recipe, substitute_recipe
from gemini.nutrients import nutritional_value

filters = ['high protein', 'low fat', 'no peanuts']
missing = ['potatoes']
available = ['carrots']

class FormState(rx.State):
    form_data: dict = {}
    lines = []
    recipe = ""
    ingredients = ""
    loading = False

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        
        self.form_data = form_data
        self.loading= True
        filter_string = ", ".join(filters)
        yield
        recipe = generate_recipe(1, self.form_data["ingredients"], filter_string)
        self.recipe = recipe
        self.loading= False

    def recipe_info(self):
        """Test recipe_ingredients"""
        self.loading= True
        yield
        self.ingredients = self.recipe["ingredients"]
        self.loading= False


    def sub_rec(self):
        self.loading= True
        yield
        substitute_recipe(self.recipe, missing, available)
        self.loading= False

    def nut_rec(self):
        self.loading= True
        yield
        nutritional_value(self.ingredients)
        self.loading= False



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
            rx.button("Ingredients", on_click=FormState.recipe_info),
            rx.button("Substitute", on_click=FormState.sub_rec),
            rx.button("Nutrition", on_click=FormState.nut_rec),
            padding_left="250px",
            background_image="url(../chat_gradient.png)",
            background_size="cover",
            background_position="center",
            height="100vh",
        ),
        # height="calc(100vh - 90px)",
        background_color="rgba(0,0,0)",
    )
