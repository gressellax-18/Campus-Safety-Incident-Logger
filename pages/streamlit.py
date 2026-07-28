import streamlit as st

st.set_page_config(
    page_title="Programming Used",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Programming & Technologies Used")
st.write("Technologies used to develop the Campus Safety Incident Logger.")

st.divider()

# ---------------- Overview ----------------

st.subheader("📌 Project Overview")

st.info("""
Campus Safety Incident Logger is a Python-based web application developed using
the Streamlit framework. It enables students to report campus incidents,
allows administrators to manage reports, and demonstrates a simple AI-based
incident classification system.
""")

st.divider()

# ---------------- Technologies ----------------

st.subheader("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.success("🐍 Python 3.x")
    st.success("🚀 Streamlit")
    st.success("💾 SQLite Database")
    st.success("📊 Pandas")

with col2:

    st.success("🤖 AI / Machine Learning")
    st.success("🧠 Rule-Based NLP")
    st.success("📈 Data Analytics")
    st.success("☁ Streamlit Cloud")

st.divider()

# ---------------- Why Streamlit ----------------

st.subheader("🚀 Why Streamlit?")

st.write("""
✔ Fast web application development

✔ Easy integration with Python

✔ Interactive dashboard support

✔ Supports AI & Machine Learning

✔ Simple deployment on Streamlit Cloud

✔ No HTML, CSS or JavaScript required
""")

st.divider()

# ---------------- Libraries ----------------

st.subheader("📚 Python Libraries")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
🐍 streamlit

📊 pandas

💾 sqlite3
""")

with c2:
    st.info("""
🤖 scikit-learn

📦 joblib

📅 datetime
""")

with c3:
    st.info("""
📈 matplotlib (optional)

📉 plotly (optional)

📝 typing
""")

st.divider()

# ---------------- Project Modules ----------------

st.subheader("📂 Project Modules")

st.success("""
🏠 Home

📖 About

🚨 Report Incident

📄 My Reports

👨‍💼 Admin Dashboard

📊 Analytics

🤖 AI Layer

🚀 Live Demo
""")

st.divider()

# ---------------- Workflow ----------------

st.subheader("⚙ System Workflow")

st.success("""
👨‍🎓 Student

⬇

🚨 Report Incident

⬇

🤖 AI Analysis

⬇

💾 SQLite Database

⬇

👨‍💼 Admin Dashboard

⬇

📊 Analytics

⬇

📄 Student Tracks Report
""")

st.divider()

# ---------------- Advantages ----------------

st.subheader("🌟 Advantages")

col1, col2 = st.columns(2)

with col1:

    st.success("✔ User Friendly Interface")
    st.success("✔ Fast Performance")
    st.success("✔ Secure Database")

with col2:

    st.success("✔ Easy Deployment")
    st.success("✔ AI Ready")
    st.success("✔ Scalable Architecture")

st.divider()

# ---------------- Footer ----------------

st.success("🎉 Campus Safety Incident Logger developed using Python & Streamlit")

st.caption("Department of Artificial Intelligence and Data Science | KIET | JNTUK")