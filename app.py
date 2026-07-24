import streamlit as st
from database import create_table

# Create database table when app starts
create_table()

st.set_page_config(
    page_title="Campus Safety Incident Logger",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Campus Safety Incident Logger")

st.markdown("""
## Welcome 👋

This application helps students report campus safety incidents.

Use the **sidebar** to navigate through the project.
""")

st.success("Project Started Successfully ✅")