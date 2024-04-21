from gemini.base import model
import json
from IPython.display import Image

def parse_health_stats():
    image = Image(filename="assets/health_record.png")
    prompt = """
    Please return a JSON object containing the keys for what was being tested and the result and units as the value.

    The object should follow the structure:
    \{{"LDL Cholesterol": "83 mg/DL"}}

    Here is the given file:
    """
    response = model.generate_content([prompt, image])
    print(response.text)


# based on the input of the data numbeers, age, json object that defines if a user is in a good spot or no
def evaluate_health(user_info, health_record):
    prompt = f"""
    Please return a JSON of an evaluation on a user's health record. 

    A user's physical attributes should influence whether their health record number is "too low", "low", "just right", "high", "too high" relative to the healthy ranges.

    The user's information is listed here. The major influencing factors are age and weight:

    {user_info}

    The output JSON should follow this schema for each test:
    \{{"iron": \{{"score": NUMBER, "status": CONDITION}}}}
    CONDITION follows "too low", "too high", or "just right".

    Here is the health record to base the evaluations on:

    {health_record}
    """
    response = model.generate_content(prompt)
    evaluation = json.loads(response.text)
    print(response.text)
    return evaluation[0]

# create an action plan for certain categories to avoid
