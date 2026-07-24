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
        status = report[4]
        remarks = report[5]

        st.markdown(f"### Report ID : {incident_id}")

        st.write(f"**Description:** {description}")
        st.write(f"**Category:** {category}")
        st.write(f"**Location:** {location}")

        if status == "Pending":
            st.warning("🟡 Status : Pending")

        elif status == "In Progress":
            st.info("🔵 Status : In Progress")

        elif status == "Resolved":
            st.success("🟢 Status : Resolved")

        if remarks:
            st.write(f"**Remarks:** {remarks}")

        st.markdown("---")

else:
    st.info("No reports found.")