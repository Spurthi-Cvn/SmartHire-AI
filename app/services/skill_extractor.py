SKILLS = [
    "AWS",
    "Docker",
    "Kubernetes",
    "Terraform",
    "Jenkins",
    "Python",
    "SQL",
    "Git",
    "Linux",
    "Ansible",
    "FastAPI",
    "PostgreSQL"
]


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills