import streamlit as st
from database import (
    create_table,
    get_incidents,
    update_incident_status
)

# Create database table
create_table()

# -------------------------------
# Simple Admin Login
# -------------------------------
ADMIN_PASSWORD = "admin123"

st.title("🔐 Admin Login")

password = st.text_input("Enter Admin Password", type="password")

if password != ADMIN_PASSWORD:
    st.warning("Please enter the correct admin password.")
    st.stop()

# -------------------------------
# Admin Dashboard
# -------------------------------

st.title("🛠️ Admin Dashboard")

reports = get_incidents()

st.subheader("📋 All Reported Incidents")

if reports:

    for report in reports:

        incident_id = report[0]
        description = report[1]
        category = report[2]
        location = report[3]
        status = report[4]
        remarks = report[5]

        st.markdown(f"### 🚨 Incident ID : {incident_id}")

        st.write(f"**Description:** {description}")
        st.write(f"**Category:** {category}")
        st.write(f"**Location:** {location}")

        # Status Color
        if status == "Pending":
            st.warning("🟡 Pending")

        elif status == "In Progress":
            st.info("🔵 In Progress")

        elif status == "Resolved":
            st.success("🟢 Resolved")

        # Update Status
        new_status = st.selectbox(
            "Update Status",
            ["Pending", "In Progress", "Resolved"],
            index=["Pending", "In Progress", "Resolved"].index(status),
            key=f"status_{incident_id}"
        )

        # Remarks
        new_remarks = st.text_area(
            "Resolution Remarks",
            value=remarks if remarks else "",
            key=f"remarks_{incident_id}"
        )

        # Update Button
        if st.button("✅ Update", key=f"update_{incident_id}"):

            update_incident_status(
                incident_id,
                new_status,
                new_remarks
            )

            st.success("Status Updated Successfully")
            st.rerun()

        st.markdown("---")

else:
    st.info("No incidents reported yet.")