# from IPython.display import Image
from gemini.base import model
import json

# Scans an image to structure the user's health record
def parse_health_stats(image):
    prompt = """
    Please return a JSON object containing the keys for what was being tested and the result and units as the value.

    The object should follow the structure:
    \{{"LDL Cholesterol": "83 mg/DL"}}

    Only record the following fields as keys:
    HDL_Cholesterol, LDL_Cholesterol, Triglycerides, Glucose, Sodium, Potassium, Chloride, Carbon_dioxide, Calcium, Protein, Lipoprotein: str

    Here is the given file:
    """
    response = model.generate_content([prompt, image])
    print(response.text)

# Based on a user's health record, evaluate if there are concerns for certain tests
def evaluate_health(user_info, health_record):
    prompt = f"""
    Please return a JSON of an evaluation on a user's health record. 

    A user's physical attributes should influence whether their health record number is "too low", "low", "just right", "high", "too high" relative to the healthy ranges.

    The user's information is listed here. The major influencing factors are age and weight:

    {user_info}

    The output JSON should follow this schema for each test:
    \{{"HDL_Cholesterol": \{{"score": NUMBER, "status": CONDITION}}}}
    CONDITION follows "too low", "too high", or "just right".

    Here is the health record to base the evaluations on:

    {health_record}
    """
    response = model.generate_content(prompt)
    evaluation = json.loads(response.text)
    print(response.text)
    return evaluation[0]

# Create a unique plan that addresses health concerns
def create_plan(health_evaluation):
    prompt = f"""
    Please return a JSON of suggested actions to change an individual's lifestyle.

    Given an evaluation of records for different tests, give general dietary suggestions for results that are too low or too high.
    Ensure the suggestions address in improving these areas gradually.

    Here is the health evaluation with the test statuses:

    {health_evaluation}
    """
    response = model.generate_content(prompt)
    plan = json.loads(response.text)
    print(response.text)
    return plan[0]

# Give advice based on a health question
def health_advice(question):
    prompt = f"""
    Please return an array of 3 recommendations to address a health concern/question. 
    It must be constructive and feasible to improve one's lifestyle slowly.

    Here is the question:
    {question}
    """
    response = model.generate_content(prompt)
    advice = json.loads(response.text)
    print(response.text)
    return advice[0]