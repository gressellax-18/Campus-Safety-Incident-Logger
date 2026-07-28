import streamlit as st

st.set_page_config(page_title="About", page_icon="📖", layout="wide")

# ---------------- CSS ----------------

st.markdown("""
<style>

.title{
font-size:42px;
font-weight:bold;
color:#d32f2f;
text-align:center;
}

.subtitle{
text-align:center;
color:gray;
font-size:20px;
margin-bottom:25px;
}

.card{
background:#ffffff;
padding:20px;
border-radius:15px;
box-shadow:0px 6px 15px rgba(0,0,0,0.12);
margin-bottom:18px;
}

.problem{
background:#fff3cd;
padding:18px;
border-left:8px solid orange;
border-radius:10px;
}

.solution{
background:#d4edda;
padding:18px;
border-left:8px solid green;
border-radius:10px;
}

</style>
""",unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown('<p class="title">📖 About Project</p>',unsafe_allow_html=True)

st.markdown('<p class="subtitle">AI Powered Campus Safety Management System</p>',unsafe_allow_html=True)

st.divider()

# ---------------- OVERVIEW ----------------

st.markdown("""

<div class="card">

### 🎯 Project Overview

Campus Safety Incident Logger is a smart web application developed to help
students report safety-related incidents quickly and securely.

The system enables students to submit complaints digitally while allowing
administrators to review, investigate and resolve incidents efficiently.

It provides transparency, faster response and better campus safety.

</div>

""",unsafe_allow_html=True)

# ---------------- PROBLEM ----------------

st.subheader("🚨 Problem Statement")

st.markdown("""

<div class="problem">

❌ Paper-based complaint systems

❌ Delay in reporting incidents

❌ No complaint tracking

❌ Lack of transparency

❌ Slow administrative response

❌ Students hesitate to report issues

</div>

""",unsafe_allow_html=True)

st.divider()

# ---------------- SOLUTION ----------------

st.subheader("💡 Proposed Solution")

st.markdown("""

<div class="solution">

✔ Digital Incident Reporting

✔ AI Based Classification

✔ Complaint Tracking

✔ Admin Dashboard

✔ Status Updates

✔ Safe & Secure Database

✔ Better Communication

</div>

""",unsafe_allow_html=True)

st.divider()

# ---------------- OBJECTIVES ----------------

st.subheader("🎯 Objectives")

c1,c2=st.columns(2)

with c1:

    st.success("📌 Improve Campus Safety")

    st.success("📌 Digital Complaint System")

    st.success("📌 Paperless Process")

with c2:

    st.success("📌 Faster Resolution")

    st.success("📌 Complaint Transparency")

    st.success("📌 AI Integration")

st.divider()

# ---------------- BENEFITS ----------------

st.subheader("🌟 Benefits")

col1,col2,col3=st.columns(3)

with col1:

    st.info("""

👨‍🎓 Students

• Easy Reporting

• Complaint Tracking

• Faster Help

""")

with col2:

    st.info("""

👮 Management

• Central Dashboard

• Better Monitoring

• Quick Action

""")

with col3:

    st.info("""

🏫 Campus

• Safer Environment

• Digital Records

• Better Security

""")

st.divider()

# ---------------- WORKFLOW ----------------

st.subheader("⚙ Project Workflow")

st.success("""

👨‍🎓 Student

⬇

🚨 Report Incident

⬇

🤖 AI Categorization

⬇

💾 SQLite Database

⬇

👨‍💼 Admin Verification

⬇

📝 Status Update

⬇

📄 Student Tracking

""")

st.divider()

# ---------------- TECHNOLOGIES ----------------

st.subheader("🛠 Technologies Used")

a,b,c,d=st.columns(4)

a.metric("🐍 Python","100%")
b.metric("🌐 Streamlit","UI")
c.metric("💾 SQLite","Database")
d.metric("🤖 AI/ML","Future Ready")

st.divider()

# ---------------- FOOTER ----------------

st.markdown("""
<center>

### ❤️ Campus Safety Incident Logger

Making College Campuses Safer with Technology

</center>
""",unsafe_allow_html=True)