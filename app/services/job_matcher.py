def calculate_match_percentage(
    resume_skills,
    required_skills
):

    matched_skills = []

    for skill in required_skills:

        if skill in resume_skills:
            matched_skills.append(skill)

    percentage = round(
        (len(matched_skills) / len(required_skills)) * 100,
        2
    )

    return matched_skills, percentage