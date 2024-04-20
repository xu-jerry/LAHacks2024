from gemini.base import model
import json

# Generate a recipe based on the available ingredients
#TODO: add parameters that account for individual health requests
#TODO: add parameter to keep track of the number of recipes to generate?
def generate_recipe(ingredients):
    prompt = f"List out some full recipes with {ingredients} as ingredients."
    response = model.generate_content(prompt)
    recipe = response.text
    return recipe

# Parse the ingredients and quantities from a given recipe
def recipe_ingredients(recipe):
    prompt = """
    Please return a JSON of the ingredients and quantities from a given recipe in the following schema:
    {ingredient: quantity}

    The ingredient in the recipe is the key and the quantity is the value. Both are strings.

    Important: Only return a single piece of valid JSON text.

    Here is the recipe:

    """
    response = model.generate_content(prompt + recipe)
    print(response.text)
    recipe_info = json.loads(response.text)
    return recipe_info

#replace with preferences
#replace with existing ingredients