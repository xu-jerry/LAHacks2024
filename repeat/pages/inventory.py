import reflex as rx
from typing import List, Dict, Tuple
from ..state.base import State

from repeat.template import template

class Appliances(rx.State):
    appliances: List[str] = ['Fridge', 'Microwave', 'Oven']

class Foods(rx.State):
    foods: Dict[str, List[str]] = {
        'Carbohydrates': ['Rice', 'Brown Rice', 'White Bread', 'Whole Wheat Bread'], 
        'Vegetables': ['Garlic', 'Chili Pepper', 'Tomato', 'Carrot', 'Potato'],
        'Proteins': ['Chicken', 'Pork', 'Tofu', 'Eggs'],
        'Dairy': ['Yogurt', 'Ricotta'],
        'Fruits': ['Blueberries', 'Strawberries'],
        'Other': ['Salt', 'Pepper', 'Hot Sauce']
    }

    @rx.var
    def cur_foods(self) -> Dict[str, Dict[str, bool]]:
        return {key : {name: False for name in value} for key, value in self.foods.items()}

    def update_local_inventory(self, category: str, food: str, selected: bool):
        self.cur_foods[category][food] = ~selected
        rx.console_log("hi")
        
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
                  rx.hstack(
                      rx.foreach(food_group[1],
                                 lambda food: rx.cond(
                                     food[1],
                                     rx.button(food[0],
                                               color="rgba(255,0,0,1)",
                                               on_click=lambda: Foods.update_local_inventory(Foods, food_group[0].to_string(), food[0].to_string(), food[1])),
                                               rx.button(food),
                                )
                       )
                   ),
    )

class Test(rx.State):
    def test1(self):
        print("hello1")
        print(State.user)
        print(State.user.to_string())

def test2():
    rx.console_log("Hello World!")


@template
def inventory() -> rx.Component:
    return rx.box(
            rx.box(
                rx.text("Inventory"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            rx.button("test1", on_click=Test.test1),
            rx.button("test2", on_click=rx.console_log(State.user)),
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
