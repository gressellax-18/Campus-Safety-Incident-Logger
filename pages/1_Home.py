import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main-title{
    font-size:42px;
    font-weight:bold;
    color:#d32f2f;
    text-align:center;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:20px;
    margin-bottom:25px;
}

.card{
    background-color:#ffffff;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.15);
    margin-bottom:15px;
}

.feature{
    background:#f8f9fa;
    padding:15px;
    border-left:6px solid #d32f2f;
    border-radius:10px;
    margin-bottom:12px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown('<p class="main-title">🚨 Campus Safety Incident Logger</p>', unsafe_allow_html=True)

st.markdown(
'<p class="sub-title">Protect • Report • Resolve</p>',
unsafe_allow_html=True
)

st.success("🎓 AI Powered Smart Campus Safety Management System")

st.divider()

# ---------------- DASHBOARD ----------------

st.subheader("📊 Project Highlights")

c1,c2,c3,c4=st.columns(4)

c1.metric("📄 Modules","9")
c2.metric("🤖 AI Ready","Yes")
c3.metric("💾 Database","SQLite")
c4.metric("🚀 Version","2.0")

st.divider()

# ---------------- ABOUT ----------------

st.subheader("📌 About The Project")

st.markdown("""
<div class="card">

Campus Safety Incident Logger is a smart web application developed to improve
student safety inside college campuses.

Students can report incidents instantly and the administration can review,
investigate and resolve them through a centralized dashboard.

The entire complaint process becomes digital, transparent and easy to track.

</div>
""",unsafe_allow_html=True)

st.divider()

# ---------------- INCIDENT TYPES ----------------

st.subheader("🚨 Incident Categories")

col1,col2,col3=st.columns(3)

with col1:
    st.error("🚨 Ragging")
    st.error("🚲 Theft")

with col2:
    st.warning("🔥 Fire Accident")
    st.warning("🏥 Medical Emergency")

with col3:
    st.info("⚠ Suspicious Activity")
    st.info("👊 Harassment")

st.divider()

# ---------------- OBJECTIVES ----------------

st.subheader("🎯 Project Objectives")

c1,c2=st.columns(2)

with c1:

    st.markdown("""
<div class="feature">

✅ Digital Complaint Reporting

</div>

<div class="feature">

✅ Faster Response

</div>

<div class="feature">

✅ Student Safety

</div>
""",unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class="feature">

✅ Paperless System

</div>

<div class="feature">

✅ Complaint Tracking

</div>

<div class="feature">

✅ Centralized Database

</div>
""",unsafe_allow_html=True)

st.divider()

# ---------------- FEATURES ----------------

st.subheader("✨ System Features")

a,b,c=st.columns(3)

with a:
    st.success("🔐 Secure Login")
    st.success("🚨 Report Incident")
    st.success("📄 My Reports")

with b:
    st.success("👨‍💼 Admin Dashboard")
    st.success("📊 Analytics")
    st.success("🤖 AI Classification")

with c:
    st.success("📍 Incident Tracking")
    st.success("📝 Status Updates")
    st.success("📢 Management Remarks")

st.divider()

# ---------------- WORKFLOW ----------------

st.subheader("⚙ System Workflow")

st.info("""

👨‍🎓 Student

⬇

🚨 Report Incident

⬇

🤖 AI Classifies Incident

⬇

💾 Stored in Database

⬇

👨‍💼 Admin Reviews

⬇

📝 Status Updated

⬇

📄 Student Tracks Report

""")

st.divider()

# ---------------- FUTURE ----------------

st.subheader("🚀 Future Enhancements")

col1,col2=st.columns(2)

with col1:

    st.success("📱 Mobile Application")

    st.success("📍 Live GPS Location")

    st.success("📧 Email Notifications")

with col2:

    st.success("📸 Image Upload")

    st.success("🤖 Advanced AI Model")

    st.success("🔔 Real-time Alerts")

st.divider()

st.markdown(
"""
<div class="footer">

❤️ Developed using Python | Streamlit | SQLite | Machine Learning

</div>
""",
unsafe_allow_html=True
)