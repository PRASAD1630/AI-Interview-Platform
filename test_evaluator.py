from services.evaluator import evaluate_answer

question = "What is Machine Learning?"

answer = """
Machine Learning is a field of AI
that learns patterns from data.
"""

result = evaluate_answer(
    question,
    answer
)

print(result)