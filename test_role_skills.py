from services.role_skill_generator import get_role_skills

skills = get_role_skills(
    "Data Scientist"
)

print(skills)