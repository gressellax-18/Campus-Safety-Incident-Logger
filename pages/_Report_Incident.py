import streamlit as st
from database import add_incident

st.title("Report Incident")

description = st.text_area("Incident Description")
category = st.selectbox(
    "Category",
    ["Ragging", "Harassment", "Theft", "Medical", "Other"]
)
location = st.text_input("Location")

if st.button("Submit Incident"):
    if description and category and location:
        add_incident(description, category, location)
        st.success("Incident reported successfully!")
    else:
        st.error("Please fill all fields.")
        