from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(
    resume_text,
    job_description,
    matched_skills,
    total_skills
):

    # -----------------------------------------
    # COSINE SIMILARITY
    # -----------------------------------------

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    cosine_score = similarity * 100

    # -----------------------------------------
    # SKILL SCORE
    # -----------------------------------------

    matched_count = len(matched_skills)

    # STRONG BOOST FOR MATCHED SKILLS

    skill_score = matched_count * 18

    # -----------------------------------------
    # FINAL SCORE
    # -----------------------------------------

    final_score = (
        cosine_score * 0.2
        +
        skill_score * 0.8
    )

    # -----------------------------------------
    # BONUS BOOSTS
    # -----------------------------------------

    important_skills = [
        "Python",
        "Machine Learning",
        "NLP",
        "FastAPI",
        "Scikit-learn"
    ]

    bonus = 0

    for skill in important_skills:

        if skill in matched_skills:
            bonus += 5

    final_score += bonus

    # -----------------------------------------
    # LIMIT SCORE
    # -----------------------------------------

    if final_score > 95:
        final_score = 95

    return round(final_score, 2)