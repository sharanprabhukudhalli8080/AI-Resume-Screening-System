import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.classifier import predict_category

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------

st.title("📄 AI Resume Screening System")
st.markdown(
    "Upload your resume and compare it against a Job Description using AI."
)

st.divider()

# -----------------------------
# INPUT SECTION
# -----------------------------

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

# -----------------------------
# PROCESSING
# -----------------------------

if uploaded_resume and job_description:

    # Extract Resume Text
    resume_text = extract_text_from_pdf(
        uploaded_resume
    )

    # Extract Skills
    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        job_description
    )

    # ATS Score
    score, matched_skills, missing_skills = calculate_ats_score(
        resume_skills,
        jd_skills
    )

    # Resume Category Prediction
    predicted_category = predict_category(
        resume_text
    )

    st.divider()

    # -----------------------------
    # TOP METRICS
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="ATS Score",
            value=f"{score}%"
        )

    with col2:
        st.metric(
            label="Predicted Category",
            value=predicted_category
        )

    st.divider()

    # -----------------------------
    # SKILLS FOUND
    # -----------------------------

    st.subheader("📌 Skills Found in Resume")

    if resume_skills:
        st.success(", ".join(resume_skills))
    else:
        st.warning("No skills found.")

    # -----------------------------
    # MATCHED SKILLS
    # -----------------------------

    st.subheader("✅ Matched Skills")

    if matched_skills:
        st.success(", ".join(matched_skills))
    else:
        st.warning("No matching skills found.")

    # -----------------------------
    # MISSING SKILLS
    # -----------------------------

    st.subheader("❌ Missing Skills")

    if missing_skills:
        st.error(", ".join(missing_skills))
    else:
        st.success("Great! No missing skills.")

    # -----------------------------
    # RESUME TEXT
    # -----------------------------

    with st.expander("View Extracted Resume Text"):
        st.write(resume_text)

    # -----------------------------
    # RECOMMENDATIONS
    # -----------------------------

    st.subheader("💡 Suggestions")

    if score >= 80:
        st.success(
            "Your resume is highly aligned with the Job Description."
        )

    elif score >= 60:
        st.warning(
            "Your resume matches moderately. Consider adding missing skills."
        )

    else:
        st.error(
            "Low ATS score. Update your resume with relevant skills."
        )

    if missing_skills:

        st.write("Recommended Skills to Add:")

        for skill in missing_skills:
            st.write(f"• {skill}")