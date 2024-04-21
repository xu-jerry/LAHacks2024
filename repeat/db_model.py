import reflex as rx
from typing import List

from sqlmodel import Field 

class Health_Record(rx.Model):
    """Model of Health Records"""
    HDL_Cholesterol: float
    LDL_Cholesterol: float
    Triglycerides: float
    Glucose: float
    Sodium: float
    Potassium: float
    Chloride: float
    Carbon_dioxide: float
    Calcium: float
    Protein: float
    Lipoprotein: float

class Ingredients(rx.Model):
    """Model of Ingredients"""
    ingredient: str
    quantity: float
    unit: str

class Recipe(rx.Model):
    """Model of Recipes"""
    name: str
    time: str
    ingredients: List[Ingredients]
    instructions: List[str]


class User(rx.Model, table=True):
    """A table of Users."""

    username: str = Field(primary_key=True)
    password: str
    inventory_ingredients: List[str]
    age: int
    gender: str
    weight: str
    health_record: Health_Record
    recipes: List[Recipe]
