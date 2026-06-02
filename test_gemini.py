from services.question_generator import generate_questions

skills = """
Python
SQL
Machine Learning
Flask
"""

questions = generate_questions(skills)

print(questions)