def load_skills(skills_file):
    with open(skills_file, "r", encoding="utf-8") as file:
        skills = [line.strip() for line in file.readlines()]

    return skills


def extract_skills(text, skills_list):
    matched_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            matched_skills.append(skill)

    return matched_skills