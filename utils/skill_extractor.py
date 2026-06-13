import pandas as pd

def extract_skills(text):

    skills_df = pd.read_csv("data/skills.csv")

    skills_list = skills_df["skill"].tolist()

    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))