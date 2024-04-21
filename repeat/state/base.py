"""Base state"""
from typing import Optional

import reflex as rx
from repeat.db_model import User

class State(rx.State):
    """The base state for the app."""

    user: Optional[User] =  {
    "username": "Jerames",
    "password": "password",
    "age": 22,
    "gender": "male",
    "weight": "188lbs",
    "goals": [
    {
        "name": "Creatine, Serum",
        "score": 1.44,
        "status": "too high",
        "action": "Reduce protein intake, especially red meat, and increase water intake."
    },
    {
        "name": "eGFR",
        "score": 51,
        "status": "too low",
        "action": "Consult a doctor or a registered dietitian to assess kidney function and discuss dietary changes to support kidney health, such as reducing sodium and phosphorus intake."
    }
    ],
    "grocery_list": [],
    "inventory_ingredients": "chicken, broccoli",
    "health_restrictions": "high LDL cholesterol levels, high sodium levels"
}

    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect("/login")

    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user is not None