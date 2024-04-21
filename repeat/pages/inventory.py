import reflex as rx
from typing import List, Dict, Tuple
from ..state.base import State

from repeat.template import template

import json

class Appliances(rx.State):
    appliances: List[str] = ['fridge', 'microwave', 'oven', 'toaster', 'airfryer']

foods: Dict[str, List[str]] = {
    'Carbohydrates': ['Rice', 'Brown Rice', 'White Bread', 'Whole Wheat Bread', 'Instant Ramen', 'Noodles', 'Flour', 'Nuts', 'Pasta', 'Cereal', 'Granola', "Beans", 'Legumes', 'Oats'], 
    'Vegetables': ['Garlic', 'Chili Pepper', 'Tomato', 'Carrot', 'Potato', 'Bell Pepper', 'Red Onion', 'Celery', 'Broccoli', 'Bok Choy', 'Leek', 'Sweet Potato', 'Peas', 'Spinach', 'Okra'],
    'Proteins': ['Chicken', 'Pork', 'Tofu', 'Eggs', 'Goose', 'Duck', 'Fish', 'Clams', 'Mussels', 'Oysters', 'Prawn', 'Lobster', 'Scallops', 'Crab', 'Veal', 'Goat'],
    'Dairy': ['Yogurt', 'Ricotta', 'Milk', 'Butter', 'Cream', 'Ice Cream', 'Frozen Yogurt', 'Cottage Cheese', 'Chocolate Milk', 'Custard', 'Gelato', 'Cheddar Cheese', 'Blue Cheese'],
    'Fruits': ['Blueberries', 'Strawberries', 'Apples', 'Bananas', 'Cherries', 'Dragonfruits', 'Lemon', 'Orange', 'Apricot', 'Figs', 'Cranberry', 'Blackberry', 'Honeydew Melon'],
    'Other': ['Salt', 'Pepper', 'Hot Sauce', 'Ketchup', 'Mustard', 'Relish', 'Wasabi', 'Vinegar', 'Soy Sauce', 'Wasabi', 'Pepper', 'Cinnamon', 'Parsley', 'Barbecue Sauce', 'Oil']
}

class Foods(rx.State):
    cur_foods: Dict[str, Dict[str, bool]] = {key : {name: False for name in value} for key, value in foods.items()}
    num_foods: Dict[str, int] = {key : 0 for key in foods.keys()}

    def update_local_inventory(self, category: str, food: str, selected: bool):
        self.cur_foods[category][food] = not selected
        if selected:
            self.num_foods[category] -= 1
        else:
            self.num_foods[category] += 1
        
def update_inventory():
    pass
    # with rx.session() as session:
    #         user = session.exec(
    #             select(User).where(User.username == self.username)
    #         ).first()
    #         if user and user.password == self.password:
    #             self.user = user
    #             return rx.redirect("/")
    #         else:
    #             return rx.window_alert("Invalid username or password.")



def make_category(food_group: List):
    return rx.box(
        rx.hstack(
            rx.text(food_group[0]),
            rx.text(Foods.num_foods[food_group[0].to_string()[1:-1]],
                    color="gray"),
            rx.cond(
                Foods.num_foods[food_group[0].to_string()[1:-1]] == 1,
                rx.text(" ingredient", color="gray"),
                rx.text(" ingredients", color="gray"),
            ),
            margin_bottom="10px",
        ),
        rx.hstack(
            rx.foreach(food_group[1],
                        lambda food: rx.cond(
                            food[1],
                            rx.button(food[0],
                                    background_color="rgba(255, 255, 255, 0.3)",
                                    on_click=lambda: Foods.update_local_inventory(food_group[0], food[0], food[1])),
                            rx.button(food[0],
                                    background_color="rgba(255, 255, 255, 0.08)",
                                    on_click=lambda: Foods.update_local_inventory(food_group[0], food[0], food[1])),
                    )
            ),
            margin_bottom="10px",
        ),
    )

@template
def inventory() -> rx.Component:
    return rx.box(
              rx.box(
                rx.text("Inventory",font_size="2em",),
                margin_top="calc(50px + 2em)",
                padding_left="1em",
                padding_bottom="1em",
                font_size="35px",
              ),
            rx.box(
                rx.text("Appliances", font_weight="bold",),
                margin_top="2em",
                margin_bottom="1em",
            ),
            rx.hstack(
                rx.foreach(Appliances.appliances, lambda appliance: rx.image(src="/inventory/" + appliance + ".svg", width="15em"),),
                margin_bottom="4em",
            ),
            rx.box(
                rx.text("Pantry", font_weight="bold",),
                margin_top="2em",
                margin_bottom="1em",
            ),
            rx.foreach(Foods.cur_foods, make_category),
            padding_left="250px",
            padding_right="250px",
            color="rgba(255,255,255,1)",
        )
