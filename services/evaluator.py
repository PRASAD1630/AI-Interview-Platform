import google.generativeai as genai
from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def evaluate_answer(question, answer):

    prompt = f"""
    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer.

    Give:

    Technical Score (out of 10)

    Communication Score (out of 10)

    Suggestions

    Overall Feedback
    """

    response = model.generate_content(prompt)

    return response.text