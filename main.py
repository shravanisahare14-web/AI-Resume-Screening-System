import os

from src.extractor import (
    extract_pdf_text,
    extract_docx_text
)

from src.cleaner import clean_text

from src.matcher import (
    load_skills,
    extract_skills
)

from src.scorer import calculate_similarity

from src.report_generator import generate_report


# ------------------------------------------------
# LOAD JOB DESCRIPTION
# ------------------------------------------------

with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as file:

    job_description = file.read()

cleaned_jd = clean_text(job_description)

# ------------------------------------------------
# LOAD SKILLS
# ------------------------------------------------

skills = load_skills(
    "data/skills.txt"
)

# ------------------------------------------------
# RESUME FOLDER
# ------------------------------------------------

resume_folder = "resumes"

results = []

# ------------------------------------------------
# PROCESS EACH RESUME
# ------------------------------------------------

for file_name in os.listdir(resume_folder):

    file_path = os.path.join(
        resume_folder,
        file_name
    )

    resume_text = ""

    # --------------------------------------------
    # PDF EXTRACTION
    # --------------------------------------------

    if file_name.endswith(".pdf"):

        resume_text = extract_pdf_text(
            file_path
        )

    # --------------------------------------------
    # DOCX EXTRACTION
    # --------------------------------------------

    elif file_name.endswith(".docx"):

        resume_text = extract_docx_text(
            file_path
        )

    else:
        continue

    # --------------------------------------------
    # CLEAN RESUME TEXT
    # --------------------------------------------

    cleaned_resume = clean_text(
        resume_text
    )

    # --------------------------------------------
    # EXTRACT MATCHED SKILLS
    # --------------------------------------------

    matched_skills = extract_skills(
        resume_text,
        skills
    )

    # --------------------------------------------
    # CALCULATE ATS SCORE
    # --------------------------------------------

    score = calculate_similarity(
        cleaned_resume,
        cleaned_jd,
        matched_skills,
        len(skills)
    )

    # --------------------------------------------
    # SHORTLIST DECISION
    # --------------------------------------------

    decision = (
        "Shortlisted"
        if score >= 50
        else "Rejected"
    )

    # --------------------------------------------
    # STORE RESULTS
    # --------------------------------------------

    results.append({

        "Candidate": file_name,

        "Score": score,

        "Matched Skills": ", ".join(
            matched_skills
        ),

        "Decision": decision
    })

# ------------------------------------------------
# GENERATE REPORT
# ------------------------------------------------

output_path = (
    "outputs/ranking_report.csv"
)

report_df = generate_report(
    results,
    output_path
)

# ------------------------------------------------
# DISPLAY RESULTS
# ------------------------------------------------

print("\n===== ATS SCREENING RESULTS =====\n")

print(report_df)

print(
    f"\nReport Saved At: {output_path}"
)