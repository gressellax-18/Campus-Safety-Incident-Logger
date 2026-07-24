import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("🏫 Campus Safety Incident Logger")

st.markdown("---")

st.header("📌 About the Project")

st.write("""
Campus Safety Incident Logger is a web application developed using Streamlit
to help students report safety-related incidents inside the college campus.

Students can report incidents like:

- 🚨 Ragging
- 🚲 Theft
- 🔥 Fire Accidents
- 🏥 Medical Emergencies
- ⚠️ Suspicious Activities
- 👊 Harassment

The reported incidents are stored in a database and reviewed by the Admin.
The Admin updates the status, and students can track their reports.
""")

st.markdown("---")

st.header("🎯 Project Objectives")

st.markdown("""
✅ Digital Incident Reporting

✅ Improve Campus Safety

✅ Faster Complaint Process

✅ Centralized Database

✅ Easy Incident Tracking

✅ Paperless Complaint System
""")

st.markdown("---")

st.header("💡 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("🔐 Secure Login")
    st.success("🚨 Report Incident")
    st.success("📄 Track Complaint")

with col2:
    st.success("👮 Admin Dashboard")
    st.success("📊 Analytics")
    st.success("🤖 AI Future Enhancement")

st.markdown("---")

st.info("Developed using ❤️ Python + Streamlit")
