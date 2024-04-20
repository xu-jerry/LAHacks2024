from gemini.base import model
import json

# Return nutrional value of ingredients and their quantity
#TODO: adjust to account for the different categories
def nutritional_value(ingredients):
    prompt = f"""
    Please return a JSON of the nutritional contents and quantities with measurement units from a given object of ingredients with the following keys:
    protein, carbohydrate, sugar, vegetables, fruits, sodium, water

    The values can be estimated be based on the average contents.

    Important: Only return a single piece of valid JSON text.

    Here are the ingredients:

    {ingredients}
    """
    response = model.generate_content(prompt)
    nutrition = json.loads(response.text)
    print(response.text)
    return nutrition[0]


# given the food group counts, determine if they will impact the health levels