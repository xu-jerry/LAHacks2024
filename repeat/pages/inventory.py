import reflex as rx
from typing import List, Dict, Tuple
from ..state.base import State

from repeat.template import template

import json

class Appliances(rx.State):
    appliances: List[str] = ['Fridge', 'Microwave', 'Oven']

foods: Dict[str, List[str]] = {
    'Carbohydrates': ['Rice', 'Brown Rice', 'White Bread', 'Whole Wheat Bread'], 
    'Vegetables': ['Garlic', 'Chili Pepper', 'Tomato', 'Carrot', 'Potato'],
    'Proteins': ['Chicken', 'Pork', 'Tofu', 'Eggs'],
    'Dairy': ['Yogurt', 'Ricotta'],
    'Fruits': ['Blueberries', 'Strawberries'],
    'Other': ['Salt', 'Pepper', 'Hot Sauce']
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
    return rx.box(rx.text(food_group[0]),
                  rx.text(Foods.num_foods[food_group[0].to_string()[1:-1]]),
                #   rx.text(json.loads(str(food_group[1].to_string()))),
                #   rx.text(len([k for k, v in dict(food_group[0].to_string()) if v])),
                  rx.hstack(
                      rx.foreach(food_group[1],
                                 lambda food: rx.cond(
                                     food[1],
                                     rx.button(food[0],
                                               color="rgba(255,0,0,1)",
                                               on_click=lambda: Foods.update_local_inventory(food_group[0], food[0], food[1])),
                                     rx.button(food[0],
                                               on_click=lambda: Foods.update_local_inventory(food_group[0], food[0], food[1])),
                                )
                       )
                   ),
    )

@template
def inventory() -> rx.Component:
    return rx.box(
            rx.box(
                rx.text("Inventory"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            rx.box(
                rx.text("Appliances"),
                margin_top="calc(2em)",
            ),
            rx.hstack(
                rx.foreach(Appliances.appliances, lambda appliance: rx.button(appliance)),
            ),
            rx.box(
                rx.text("Pantry"),
                margin_top="calc(2em)",
            ),
            rx.foreach(Foods.cur_foods, make_category),
            padding_left="250px",
            color="rgba(255,255,255,1)",
        )
