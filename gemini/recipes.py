from gemini.base import model
import json

# Generate a recipe based on the available ingredients
def generate_recipe(ingredients, number, filter):
    prompt = f"""
    List out {number} full recipes with the following ingredients in specific measurements and quantities:

    {ingredients}

    Structure the recipe in the given schema:

    It must be an object with the keys name, ingredients, and instructions. 
    name is a string value. 
    ingredients is an array of objects with keys ingredient, quantity, unit. ingredients must have simplified ingredient names, specific measurements in quantity and units.
    instructions are an array of strings with the step number preceding the instruction.

    Consider the following dietary restrictions when constructing the recipes:

    {filter}
    """
    response = model.generate_content(prompt)
    print(response.text)
    recipe = json.loads(response.text)
    return recipe[0]

# Replace ingredients within the recipe to maintain taste
def substitute_recipe(recipe, missing_ingredients, available_ingredients):
    prompt = f"""
    Given a recipe object, substitute the missing ingredients with the available ingredients and return only the updated recipe object.

    Here is the recipe:

    {recipe}

    Here are the missing ingredients:

    {missing_ingredients}

    Here are the available ingredients:
    
    {available_ingredients}

    If some of the missing ingredients could not be substituted, append a string to the end with the header "Ingredients to Buy".
    """
    response = model.generate_content(prompt)
    print(response.text)
    new_recipe = json.loads(response.text)
    return new_recipe[0]
