from services.ai_skill_extractor import extract_skills_ai

resume_text = """
Python
Machine Learning
SQL
Flask
AWS
"""

skills = extract_skills_ai(resume_text)

print(skills)