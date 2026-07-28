import streamlit as st
from database import create_table, get_incidents

# -----------------------------
# Database Initialization
# -----------------------------
create_table()

st.set_page_config(
    page_title="Campus Safety Incident Logger",
    page_icon="🚨",
    layout="wide"
)

# -----------------------------
# Fetch Data
# -----------------------------
reports = get_incidents()

total_reports = len(reports)
resolved = sum(1 for report in reports if report[7] == "Resolved")
pending = total_reports - resolved

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#D32F2F;'>
    🚨 Campus Safety Incident Logger
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align:center; color:gray;'>
    AI Powered Campus Incident Reporting System
    </h4>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# Dashboard Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📋 Total Reports", total_reports)

with col2:
    st.metric("✅ Resolved", resolved)

with col3:
    st.metric("⏳ Pending", pending)

st.markdown("---")

# -----------------------------
# About Project
# -----------------------------
st.subheader("📖 About Project")

st.info("""
Campus Safety Incident Logger is an AI-powered web application that allows students
to report campus safety incidents quickly and securely.

The system automatically classifies the incident using Artificial Intelligence
and stores it in the database for administrators to review.
""")

# -----------------------------
# Features
# -----------------------------
st.subheader("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("""
✔ Report Incidents

✔ AI Classification

✔ Secure SQLite Database

✔ Anonymous Friendly
""")

with col2:
    st.success("""
✔ Admin Dashboard

✔ Incident Tracking

✔ Status Updates

✔ Preventive Suggestions
""")

st.markdown("---")

# -----------------------------
# Safety Tips
# -----------------------------
st.subheader("🛡 Campus Safety Tips")

tips = [
    "🚶 Walk in well-lit areas at night.",
    "📞 Save campus emergency contacts.",
    "👥 Report suspicious activities immediately.",
    "🎒 Keep valuables secure.",
    "🚫 Avoid isolated areas after dark."
]

for tip in tips:
    st.write(tip)

st.markdown("---")

# -----------------------------
# Recent Reports
# -----------------------------
st.subheader("📑 Recent Incident Reports")

if reports:
    st.dataframe(
        reports[-5:],
        use_container_width=True
    )
else:
    st.warning("No incidents reported yet.")

st.markdown("---")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <center>

    <h4>👨‍💻 Developed Using</h4>

    Streamlit | Python | SQLite | AI / Machine Learning

    <br>

    <b>B.Tech Mini Project</b>

    </center>
    """,
    unsafe_allow_html=True
)