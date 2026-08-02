import streamlit as st

st.set_page_config(
    page_title="Campus Safety Incident Logger",
    page_icon="🛡️",
    layout="wide"
)

# Header
st.title("🛡️ Campus Safety Incident Logger")
st.subheader("AI-Powered Incident Reporting & Safety Management System")

st.markdown("---")

# Overview
st.header("📖 Overview")

st.write("""
Campus Safety Incident Logger is an intelligent safety management system
designed to improve security and incident handling within educational
institutions.

The platform allows students, faculty members, and campus authorities
to report, track, and manage safety-related incidents efficiently.

Using analytics and AI-powered insights, the system helps identify
potential risks, monitor incident trends, and support faster decision-making.

Our goal is to create a safer, smarter, and more secure campus
environment for everyone.
""")

st.markdown("---")

# Objectives
st.header("🎯 Objectives")

st.write("""
✅ Simplify incident reporting.

✅ Improve campus safety and security.

✅ Enable real-time incident monitoring.

✅ Support data-driven decision making.

✅ Maintain a centralized incident database.

✅ Provide AI-powered safety insights.

✅ Increase transparency and accountability.
""")

st.markdown("---")

# Features
st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("📝 Incident Reporting")
    st.success("📂 Incident Tracking")
    st.success("📊 Analytics Dashboard")
    st.success("📄 Report History")

with col2:
    st.success("🤖 AI Risk Analysis")
    st.success("🔐 Secure Admin Dashboard")
    st.success("📈 Trend Visualization")
    st.success("⚡ Real-Time Monitoring")

st.markdown("---")

# Advantages
st.header("🌟 Advantages")

st.write("""
🚀 Faster Reporting and Response

🛡️ Improved Campus Security

📊 Data-Driven Decision Making

🤖 AI-Powered Intelligence

🔍 Transparent Incident Tracking

📈 Better Trend Analysis

💡 Proactive Risk Prevention

🤝 Improved Communication

🌍 Future-Ready System

📚 Centralized Incident Repository
""")

st.markdown("---")

# Impact
st.header("🎓 Impact on Campus")

st.info("""
The Campus Safety Incident Logger helps institutions create a safer
environment by enabling quick reporting, efficient incident management,
and proactive safety planning.

The system improves communication between students and administrators,
reduces response time, and promotes a culture of safety and accountability.
""")

st.markdown("---")

# Footer
st.success("🛡️ Building a Safer Campus Through Technology, Analytics & AI")