import google.generativeai as genai
from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_questions(skills, role):

    prompt = f"""
    Generate 10 interview questions.

    Target Role:
    {role}

    Candidate Skills:
    {skills}

    Questions should be specific to the role.

    Return only numbered questions.
    """

    response = model.generate_content(prompt)

    return response.text