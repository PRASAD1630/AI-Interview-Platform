def extract_skills(text):

    skills_db = [

        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Flask",
        "React",
        "AWS",
        "Docker",
        "HTML",
        "CSS",
        "JavaScript",
        "Git",
        "GitHub",
        "TensorFlow",
        "PyTorch",
        "Data Science"
    ]

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return found_skills