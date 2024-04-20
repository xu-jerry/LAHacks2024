from gemini.base import model
import json

# Generate a recipe based on the available ingredients
#TODO: add parameters that account for individual health requests
#TODO: add parameter to keep track of the number of recipes to generate?
def generate_recipe(ingredients):
    prompt = """
    List out 3 full recipes with the following ingredients in specific measurements and quantities:

    """
    response = model.generate_content(prompt + ingredients)
    recipe = response.text
    print(recipe)
    return recipe

# Parse the ingredients and quantities from a given recipe
def recipe_ingredients(recipe):
    prompt = """
    Please return a JSON of the ingredients and quantities from a given recipe in the following schema:
    {ingredient: quantity}
    
    Each ingredient is simplified to its main component and each quantity contains the basic units of measurement.

    Important: Only return a single piece of valid JSON text.

    Here is the recipe:

    """
    response = model.generate_content(prompt + recipe)
    recipe_info = json.loads(response.text)
    print(recipe_info)
    return recipe_info

#replace with preferences taste
#replace with existing ingredients nution