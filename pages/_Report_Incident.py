import streamlit as st
from datetime import datetime
from database import add_incident

st.title("🚨 Report Incident")

# Incident Description
description = st.text_area("📝 Incident Description")

# Category
category = st.selectbox(
    "📂 Category",
    ["Ragging", "Harassment", "Theft", "Medical", "Other"]
)

# Location
location = st.text_input("📍 Location")

# Incident Date
incident_date = st.date_input("📅 Incident Date")

# Incident Time
incident_time = st.time_input("🕒 Incident Time")

# Reported Time (Automatic)
reported_time = datetime.now()

if st.button("Submit Incident"):

    if description and category and location:

        add_incident(
            description,
            category,
            location,
            str(incident_date),
            str(incident_time),
            reported_time.strftime("%Y-%m-%d %H:%M:%S")
        )

        st.success("✅ Incident Reported Successfully!")

    else:
        st.error("❌ Please fill all fields.")