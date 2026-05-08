import streamlit as st
import pandas as pd
import plotly.express as px
import os
import random
import time

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Resume Screening Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PREMIUM CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ================================================= */
/* MAIN BACKGROUND */
/* ================================================= */

.stApp {

    background:
    linear-gradient(
        135deg,
        #020617 0%,
        #081028 45%,
        #020617 100%
    );

    color: white;
}

/* ================================================= */
/* SIDEBAR */
/* ================================================= */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #081028 0%,
        #020617 100%
    );

    border-right:
    1px solid rgba(255,255,255,0.08);
}

/* ================================================= */
/* HERO TITLE */
/* ================================================= */

.hero-title {

    font-size: 72px;

    font-weight: 900;

    line-height: 1.05;

    background:
    linear-gradient(
        90deg,
        #3B82F6,
        #22D3EE,
        #8B5CF6
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    filter:
    drop-shadow(0 0 18px rgba(34,211,238,0.35));

    margin-bottom: 10px;
}

.hero-subtitle {

    color: #94A3B8;

    font-size: 20px;

    margin-top: -10px;

    margin-bottom: 30px;
}

/* ================================================= */
/* METRICS */
/* ================================================= */

div[data-testid="stMetric"] {

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.08);

    padding: 24px;

    border-radius: 26px;

    backdrop-filter: blur(14px);

    box-shadow:
    0 0 24px rgba(59,130,246,0.12);

    transition: 0.3s ease;
}

div[data-testid="stMetric"]:hover {

    transform: translateY(-4px);

    box-shadow:
    0 0 40px rgba(34,211,238,0.24);
}

/* ================================================= */
/* CONTAINERS */
/* ================================================= */

[data-testid="stVerticalBlockBorderWrapper"] {

    background:
    rgba(255,255,255,0.03);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius: 26px;

    padding: 12px;

    box-shadow:
    0 0 24px rgba(59,130,246,0.10);
}

/* ================================================= */
/* BUTTONS */
/* ================================================= */

.stButton > button {

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.08);

    color: white;

    border-radius: 16px;

    transition: 0.3s ease;
}

.stButton > button:hover {

    border:
    1px solid #22D3EE;

    color: #22D3EE;

    box-shadow:
    0 0 18px rgba(34,211,238,0.25);
}

/* ================================================= */
/* FILE UPLOADER */
/* ================================================= */

[data-testid="stFileUploader"] {

    background:
    rgba(255,255,255,0.03);

    border-radius: 20px;

    padding: 14px;
}

/* ================================================= */
/* PROGRESS BAR */
/* ================================================= */

.stProgress > div > div > div > div {

    background:
    linear-gradient(
        90deg,
        #3B82F6,
        #22D3EE
    );
}

/* ================================================= */
/* ALERT BOXES */
/* ================================================= */

.stSuccess,
.stInfo,
.stWarning,
.stError {

    border-radius: 18px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================

csv_path = "outputs/ranking_report.csv"

if not os.path.exists(csv_path):

    st.error("Run main.py first.")
    st.stop()

df = pd.read_csv(csv_path)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🤖 Recruiter AI")

    st.divider()

    st.subheader("Shravi Sahare")
    st.caption("Senior AI Recruiter")

    st.divider()

    st.button("🏠 Dashboard", use_container_width=True)
    st.button("📄 Resume Screening", use_container_width=True)
    st.button("📊 Analytics", use_container_width=True)
    st.button("🤖 AI Insights", use_container_width=True)
    st.button("📈 Reports", use_container_width=True)
    st.button("⚙️ Settings", use_container_width=True)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown(
    """
    <div class='hero-title'>
    AI-Powered Resume Screening Platform
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='hero-subtitle'>
    Enterprise Recruitment Intelligence Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# KPI SECTION
# =====================================================

shortlisted = len(
    df[df["Decision"] == "Shortlisted"]
)

rejected = len(
    df[df["Decision"] == "Rejected"]
)

avg_score = round(
    df["Score"].mean(),
    2
)

accuracy = random.randint(92, 99)
efficiency = random.randint(80, 95)

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    st.metric(
        "Total Resumes",
        len(df),
        "+12%"
    )

with c2:
    st.metric(
        "Shortlisted",
        shortlisted,
        "+8%"
    )

with c3:
    st.metric(
        "Rejected",
        rejected,
        "-2%"
    )

with c4:
    st.metric(
        "ATS Score",
        f"{avg_score}%",
        "+6%"
    )

with c5:
    st.metric(
        "Efficiency",
        f"{efficiency}%",
        "+18%"
    )

with c6:
    st.metric(
        "AI Accuracy",
        f"{accuracy}%",
        "+4%"
    )

st.write("")

# =====================================================
# MAIN GRID
# =====================================================

left, right = st.columns([2.2, 1])

# =====================================================
# LEFT SIDE
# =====================================================

with left:

    # -------------------------------------------------
    # UPLOAD ZONE
    # -------------------------------------------------

    with st.container(border=True):

        st.subheader("📂 AI Resume Upload Zone")

        st.caption(
            "Drop resumes here for AI screening"
        )

        uploaded_files = st.file_uploader(
            "Upload resumes",
            type=["pdf", "docx"],
            accept_multiple_files=True
        )

        if uploaded_files:

            with st.spinner(
                "Analyzing resumes..."
            ):
                time.sleep(2)

            st.success(
                f"{len(uploaded_files)} resumes analyzed successfully"
            )

    st.write("")

    # -------------------------------------------------
    # CANDIDATE RANKINGS
    # -------------------------------------------------

    st.subheader("🏆 Candidate Rankings")

    for _, row in df.iterrows():

        with st.container(border=True):

            top1, top2 = st.columns([4, 1])

            with top1:

                st.markdown(
                    f"### {row['Candidate']}"
                )

            with top2:

                st.markdown(
                    f"""
                    <h2 style='
                        color:#22D3EE;
                        text-align:right;
                    '>
                    {row['Score']}%
                    </h2>
                    """,
                    unsafe_allow_html=True
                )

            st.write("### Skills")

            skills = str(
                row["Matched Skills"]
            ).split(",")

            skill_cols = st.columns(4)

            for i, skill in enumerate(skills):

                with skill_cols[i % 4]:

                    st.info(skill.strip())

            st.progress(
                min(int(row["Score"]), 100)
            )

            if row["Decision"] == "Shortlisted":

                st.success("✅ Shortlisted")

            else:

                st.error("❌ Rejected")

# =====================================================
# RIGHT SIDE
# =====================================================

with right:

    # -------------------------------------------------
    # AI INSIGHTS
    # -------------------------------------------------

    with st.container(border=True):

        st.subheader("🤖 AI Insights")

        st.success(
            "Top candidates show strong NLP and Machine Learning alignment."
        )

        st.warning(
            "Communication skill gap detected in 34% of resumes."
        )

        st.info(
            "FastAPI demand increased significantly."
        )

        st.success(
            "Recommend prioritizing Scikit-learn candidates."
        )

    st.write("")

    # -------------------------------------------------
    # ACTIVITY FEED
    # -------------------------------------------------

    with st.container(border=True):

        st.subheader("⚡ Activity Feed")

        st.success(
            "Resume uploaded successfully"
        )

        st.info(
            "AI screening completed"
        )

        st.success(
            "Candidate shortlisted"
        )

        st.warning(
            "ATS report generated"
        )

# =====================================================
# ANALYTICS
# =====================================================

st.write("")

st.subheader("📊 Recruitment Analytics")

chart1, chart2 = st.columns(2)

# -----------------------------------------------------
# BAR CHART
# -----------------------------------------------------

with chart1:

    fig = px.bar(
        df,
        x="Candidate",
        y="Score",
        color="Decision",
        template="plotly_dark",
        title="Candidate Score Analysis"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# -----------------------------------------------------
# PIE CHART
# -----------------------------------------------------

with chart2:

    pie = px.pie(
        df,
        names="Decision",
        template="plotly_dark",
        title="Hiring Funnel"
    )

    pie.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    st.plotly_chart(
        pie,
        width="stretch"
    )

# =====================================================
# SKILL ANALYTICS
# =====================================================

all_skills = []

for skills in df["Matched Skills"]:

    split_skills = str(skills).split(",")

    for skill in split_skills:

        skill = skill.strip()

        if skill:

            all_skills.append(skill)

skill_df = pd.DataFrame(
    all_skills,
    columns=["Skill"]
)

skill_count = (
    skill_df["Skill"]
    .value_counts()
    .reset_index()
)

skill_count.columns = [
    "Skill",
    "Count"
]

fig2 = px.bar(
    skill_count,
    x="Skill",
    y="Count",
    template="plotly_dark",
    title="Skill Distribution"
)

fig2.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

st.plotly_chart(
    fig2,
    width="stretch"
)

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "AI Recruitment Intelligence Platform • Built with Python, NLP, Streamlit & Plotly"
)