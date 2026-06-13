def calculate_ats_score(resume_skills, jd_skills):

    matched_skills = []

    for skill in jd_skills:
        if skill.lower() in [s.lower() for s in resume_skills]:
            matched_skills.append(skill)

    score = (len(matched_skills) / len(jd_skills)) * 100 if jd_skills else 0

    missing_skills = list(
        set(jd_skills) - set(matched_skills)
    )

    return round(score, 2), matched_skills, missing_skills