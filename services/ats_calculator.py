from services.role_skills import ROLE_SKILLS

def calculate_ats_score(extracted_skills, role):

    role_skills = ROLE_SKILLS.get(role, [])

    matched = 0

    missing_skills = []

    for skill in role_skills:

        found = False

        for resume_skill in extracted_skills:

            if skill.lower().strip() in resume_skill.lower().strip() \
               or resume_skill.lower().strip() in skill.lower().strip():

                found = True
                matched += 1
                break

        if not found:
            missing_skills.append(skill)

    if len(role_skills) == 0:
        return 0, []

    score = int(
        (matched / len(role_skills))
        * 100
    )

    return score, missing_skills