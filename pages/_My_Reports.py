import streamlit as st
from database import create_table, get_incidents

create_table()

st.title("📄 My Reports")

reports = get_incidents()

if reports:

    for report in reports:

        incident_id = report[0]
        description = report[1]
        category = report[2]
        location = report[3]
        incident_date = report[4]
        incident_time = report[5]
        reported_time = report[6]
        status = report[7]
        remarks = report[8]

        st.markdown(f"## 🚨 Report ID : {incident_id}")

        st.write(f"**📝 Description:** {description}")
        st.write(f"**📂 Category:** {category}")
        st.write(f"**📍 Location:** {location}")
        st.write(f"**📅 Incident Date:** {incident_date}")
        st.write(f"**🕒 Incident Time:** {incident_time}")
        st.write(f"**⏰ Reported Time:** {reported_time}")

        # Status Display
        if status == "Pending":
            st.warning("🟡 Status : Pending")

        elif status == "In Progress":
            st.info("🔵 Status : In Progress")

        elif status == "Resolved":
            st.success("🟢 Status : Resolved")

        # Admin Remarks
        if remarks:
            st.write(f"**💬 Admin Remarks:** {remarks}")

        st.markdown("---")

else:
    st.info("No reports found.")