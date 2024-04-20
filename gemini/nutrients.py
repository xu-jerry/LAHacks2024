from gemini.base import model
import json

# Return nutrional value of ingredients and their quantity
def nutritional_value(ingredients):
    prompt = f"""
    Please return a JSON of the nutritional contents and quantities with measurement units from a given object of ingredients with the following keys:
    protein, carbohydrate, sugar, vegetables, fruits, sodium, water, fats, cholesterol, fiber.

    The values can be estimated be based on the ingredient contents seen on nurtrion labels.

    Important: Only return a single piece of valid JSON text.

    Here are the ingredients:

    {ingredients}
    """
    response = model.generate_content(prompt)
    nutrition = json.loads(response.text)
    print(response.text)
    return nutrition[0]

# Organize the user's grocery list into identifiable categories
def grocery_list_nutrition(items):
    prompt = f"""
    Please return a JSON of a shopping list where each key is one of the following categories:
    carbohydrates, vegetables, proteins, dairy, fruits, other.

    Sort the ingredients in this list under each of the key categories. Each value should be an array of strings

    Important: Only return a single piece of valid JSON text.

    Here is the list of items to sort:
    {items}
    """
    response = model.generate_content(prompt)
    grocery_list = json.loads(response.text)
    print(response.text)
    return grocery_list[0]

