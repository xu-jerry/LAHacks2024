from gemini.base import model
import json

# Generate a recipe based on the available ingredients
#TODO: add parameters that account for individual health requests
#TODO: add parameter to keep track of the number of recipes to generate?
def generate_recipe(ingredients, filter):
    prompt = f"""
    List out 3 full recipes with the following ingredients in specific measurements and quantities:

    {ingredients}

    Consider the following dietary restrictions when constructing the recipes:

    {filter}
    """
    response = model.generate_content(prompt)
    recipe = response.text
    print(recipe)
    return recipe

# Parse the ingredients and quantities from a given recipe
def recipe_ingredients(recipe):
    prompt = f"""
    Please return a JSON of the ingredients and quantities from a given recipe in the following schema:
    \{{ingredient: quantity}}
    
    Each ingredient is simplified to its main component and each quantity contains the basic units of measurement.

    Important: Only return a single piece of valid JSON text.

    Here is the recipe:

    {recipe}
    """
    response = model.generate_content(prompt)
    recipe_info = json.loads(response.text)
    print(recipe_info)
    return recipe_info

# Replace ingredients within the recipe to maintain taste
def substitute_recipe(recipe, missing_ingredients, available_ingredients):
    prompt = f"""
    Given a recipe, substitute the missing ingredients with the available ingredients and return the updated recipe.

    Here is the recipe:

    {recipe}

    Here are the missing ingredients:

    {missing_ingredients}

    Here are the available ingredients:
    
    {available_ingredients}

    If some of the missing ingredients could not be substituted, append a string to the end with the header "Ingredients to Buy".
    """
    response = model.generate_content(prompt)
    new_recipe = response.text
    return new_recipe
