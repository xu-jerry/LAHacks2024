from gemini.base import model
import json
# from IPython.display import Image

# Scans an image to structure the user's health record
# def parse_health_stats():
#     image = Image(filename="assets/health_record.png")
#     prompt = """
#     Please return a JSON object containing the keys for what was being tested and the result and units as the value.

#     The object should follow the structure:
#     \{{"LDL Cholesterol": "83 mg/DL"}}

#     Here is the given file:
#     """
#     response = model.generate_content([prompt, image])
#     print(response.text)

# Based on a user's health record, evaluate if there are concerns for certain tests
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

# Create a unique plan that addresses health concerns
def create_plan():
    health_evaluation = """
    [
  {"HDL Cholesterol": {"score": 58, "status": "just right"}},
  {"LDL Cholesterol": {"score": 83, "status": "just right"}}, 
  {"Triglycerides": {"score": 48, "status": "just right"}},
  {"Glucose, Serum": {"score": 99, "status": "just right"}},
  {"BUN": {"score": 20, "status": "just right"}},
  {"Creatine, Serum": {"score": 1.44, "status": "too high"}},
  {"eGFR": {"score": 51, "status": "too low"}},
  {"Sodium": {"score": 142, "status": "just right"}},
  {"Potassium": {"score": 4.2, "status": "just right"}},
  {"Chloride": {"score": 104, "status": "just right"}},
  {"Carbon dioxide": {"score": 29, "status": "just right"}}, 
  {"Calcium": {"score": 9.5, "status": "just right"}},
  {"Protein, Total": {"score": 6.6, "status": "just right"}},
  {"Albumin": {"score": 4.3, "status": "just right"}},
  {"Globulin": {"score": 2.3, "status": "just right"}},
  {"Bilirubin": {"score": 0.5, "status": "just right"}},
  {"Alkaline": {"score": 66, "status": "just right"}},
  {"AST": {"score": 14, "status": "just right"}},
  {"ALT": {"score": 18, "status": "just right"}},
  {"Lipoprotein (a)": {"score": 174, "status": "too high"}}
]
    """
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
def health_advice():
    question = """
    what ingredients should I add to my diet to Reduce protein intake, especially red meat, and increase water intake
    """
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