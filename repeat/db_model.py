import reflex as rx

from sqlmodel import Field 

class Health_Record(rx.Model, table=True):
    """Model of Health Records"""
    HDL_Cholesterol: str
    LDL_Cholesterol: str
    Triglycerides: str
    Glucose: str
    Sodium: str
    Potassium: str
    Chloride: str
    Carbon_dioxide: str
    Calcium: str
    Protein: str
    Lipoprotein: str

class Ingredients(rx.Model, table=True):
    """Model of Ingredients"""
    ingredient: str  = Field(primary_key=True)
    quantity: float
    unit: str

class Recipe(rx.Model, table=True):
    """Model of Recipes"""
    name: str  = Field(primary_key=True)
    time: str
    # List of ingredients as a concatenated string
    ingredients: str
    # List of instructions as a concatenated string
    instructions: str


class User(rx.Model, table=True):
    """A table of Users."""

    username: str = Field(primary_key=True)
    password: str
    # List of inventory ingredients as a concatenated string
    inventory_ingredients: str
    age: int
    gender: str
    weight: str
    # List of health restrictions as a concatenated string
    health_restrictions: str
    # health_record: Health_Record
