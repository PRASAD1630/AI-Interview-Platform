import google.generativeai as genai
from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_role_skills(role):

    prompt = f"""
    List the most important technical skills
    required for a {role}.

    Return only comma separated skills.

    Example:
    Python, SQL, Machine Learning
    """

    response = model.generate_content(prompt)

    return response.text