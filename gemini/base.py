import google.generativeai as genai

import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
# Export model to generate responses
model = genai.GenerativeModel('gemini-pro')