import google.generativeai as genai
from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_skills_ai(resume_text):

    prompt = f"""
    Extract technical skills from this resume.

    Resume:

    {resume_text}

    Return only a comma separated list.

    Example:
    Python, SQL, Flask, AWS
    """

    response = model.generate_content(prompt)

    return response.text