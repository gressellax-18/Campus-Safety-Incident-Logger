import streamlit as st
from datetime import datetime
from database import add_incident

st.set_page_config(
    page_title="Report Incident",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Report Campus Incident")
st.write("Fill in the details below to report a campus safety incident.")

st.divider()

col1, col2 = st.columns(2)

with col1:

    description = st.text_area(
        "📝 Incident Description",
        placeholder="Describe what happened..."
    )

    category = st.selectbox(
        "📂 Incident Category",
        [
            "Ragging",
            "Harassment",
            "Theft",
            "Medical Emergency",
            "Fire Accident",
            "Suspicious Activity",
            "Other"
        ]
    )

    location = st.text_input(
        "📍 Incident Location",
        placeholder="Example: Library, Hostel Block A"
    )

with col2:

    incident_date = st.date_input("📅 Incident Date")

    incident_time = st.time_input("🕒 Incident Time")

    st.info(f"⏰ Report Time\n\n{datetime.now().strftime('%d-%m-%Y %I:%M %p')}")

    severity = st.selectbox(
        "🚦 Severity Level",
        ["Low", "Medium", "High", "Critical"]
    )

st.divider()

st.subheader("📋 Review")

c1, c2 = st.columns(2)

with c1:
    st.write(f"**📂 Category:** {category}")
    st.write(f"**📍 Location:** {location}")
    st.write(f"**🚦 Severity:** {severity}")

with c2:
    st.write(f"**📅 Date:** {incident_date}")
    st.write(f"**🕒 Time:** {incident_time}")

st.divider()

if st.button("🚨 Submit Incident Report", use_container_width=True):

    if description.strip() == "" or location.strip() == "":

        st.error("❌ Please fill in all required fields.")

    else:

        reported_time = datetime.now()

        add_incident(
            description,
            category,
            location,
            str(incident_date),
            str(incident_time),
            reported_time.strftime("%Y-%m-%d %H:%M:%S")
        )

        st.success("✅ Incident Report Submitted Successfully!")

        st.balloons()

        st.info("""
📌 Your complaint has been submitted.

Current Status:

🟡 Pending

The management will review your report soon.
""")

st.divider()

st.subheader("📢 Reporting Guidelines")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ Provide accurate incident details.")
    st.success("✅ Mention the correct location.")
    st.success("✅ Report immediately after the incident.")

with col2:
    st.warning("❌ Do not submit false complaints.")
    st.warning("❌ Avoid duplicate reports.")
    st.warning("❌ Use respectful language.")

st.divider()

st.caption("Campus Safety Incident Logger | Student Reporting Portal")