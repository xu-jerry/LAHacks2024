import reflex as rx

from LAHacks2024.navigation import navbar
from LAHacks2024.template import template

import google.generativeai as genai

import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

@template
def recipes() -> rx.Component:
    response = model.generate_content("List out some full recipes with onion, carrots, and chicken as ingredients.")
    print(response.text)
    lines = response.text.split('\n')
    print(lines)

    return rx.box(
            navbar(heading="Recipes"),
            *map(lambda line: rx.box(
                rx.text(line),
            ), lines),

            padding_left="250px",
        )
