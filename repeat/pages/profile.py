import reflex as rx
from repeat.template import template
from ..state.base import State
from gemini.health import parse_health_stats, evaluate_health, create_plan
from gemini.nutrients import grocery_list_nutrition

class ProfileState(rx.State):
    info = {}
    goals = []
    grocery_list = []
    medical_record = {}

    def get_info(self):
        self.info = {
            "age": State.user.age,
            "gender": State.user.gender,
            "weight": State.user.weight
        }

    def get_goals(self):
        self.goals = State.user.goals
    
    def get_grocery_list(self):
        self.grocery_list = grocery_list_nutrition(State.user.grocery_list)

    def upload_record(self, image_path):
        self.medical_record = parse_health_stats(image_path)
    
    def generate_goals(self):
        evaluation = evaluate_health(self.medical_record)
        self.goals = create_plan(evaluation)

def content_grid():
    return (
        rx.chakra.grid(
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Profile", font_size="3rem", font_weight="600"
                    ),
                    rx.image(src="/dashboard/search.svg"),
                    width="100%",
                    margin_bottom="3em",
                ),
                rx.hstack(
                    rx.vstack(
                        rx.image(src="/profile/your-info.svg", margin_bottom="1em"),
                        rx.image(src="/profile/your-records.svg"),
                    ),
                    rx.vstack(
                        rx.image(src="/dashboard/goal.svg", margin_bottom="1em"),
                        rx.image(src="/profile/grocery-list.svg"),
                        margin_x="1em",
                    ),
                    rx.vstack(
                        rx.image(src="/profile/medical-info.svg"),
                    ),
                    width="100%",
                ),
            ),
        ),
    )


@template
def profile() -> rx.Component:
    return rx.box(
        rx.box(
            content_grid(),
            margin_top="calc(50px + 2em)",
            padding="3em",
        ),
        padding_x="4em",
    )
