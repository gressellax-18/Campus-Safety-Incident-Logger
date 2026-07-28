import streamlit as st
from database import create_table, get_incidents, update_incident_status

create_table()

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)

# ---------------- Login ----------------

ADMIN_PASSWORD = "admin123"

st.title("🔐 Admin Login")

password = st.text_input("Enter Password", type="password")

if password != ADMIN_PASSWORD:
    st.warning("Enter correct password")
    st.stop()

# ---------------- Dashboard ----------------

st.title("👨‍💼 Admin Dashboard")

reports = get_incidents()

# Dashboard Statistics
total = len(reports)
pending = sum(1 for r in reports if r[7] == "Pending")
progress = sum(1 for r in reports if r[7] == "In Progress")
resolved = sum(1 for r in reports if r[7] == "Resolved")

c1, c2, c3, c4 = st.columns(4)

c1.metric("📄 Total", total)
c2.metric("🟡 Pending", pending)
c3.metric("🔵 Progress", progress)
c4.metric("🟢 Resolved", resolved)

st.divider()

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

        with st.expander(f"🚨 Incident #{incident_id}"):

            st.write("**Category:**", category)
            st.write("**Location:**", location)
            st.write("**Date:**", incident_date)
            st.write("**Time:**", incident_time)
            st.write("**Reported:**", reported_time)
            st.write("**Description:**", description)

            if status == "Pending":
                st.warning("🟡 Pending")
            elif status == "In Progress":
                st.info("🔵 In Progress")
            elif status == "Resolved":
                st.success("🟢 Resolved")

            new_status = st.selectbox(
                "Update Status",
                ["Pending", "In Progress", "Resolved"],
                index=["Pending", "In Progress", "Resolved"].index(status),
                key=f"status_{incident_id}"
            )

            new_remarks = st.text_area(
                "Management Remarks",
                value=remarks,
                key=f"remarks_{incident_id}"
            )

            if st.button("✅ Update", key=f"update_{incident_id}"):

                update_incident_status(
                    incident_id,
                    new_status,
                    new_remarks
                )

                st.success("Updated Successfully")
                st.rerun()

else:
    st.info("No reports found.")