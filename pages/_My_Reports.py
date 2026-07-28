import streamlit as st
from database import create_table, get_incidents

create_table()

st.set_page_config(
    page_title="My Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 My Reports")
st.write("Track the status of your submitted incidents.")

st.divider()
search = st.text_input(
    "🔍 Search Reports",
    placeholder="Search by description..."
)


reports = get_incidents()
st.divider()

search = st.text_input(
    "🔍 Search Reports",
    placeholder="Search by incident description..."
)


if reports:

    st.metric("📋 Total Reports", len(reports))

    st.divider()

for report in reports:

    incident_id = report[0]
    description = report[1]
    category = report[2]
    location = report[3]
    incident_date = report[4]
    incident_time = report[5]
    reported_time = report[6]
    status = report[7]
    remarks = report[8] if report[8] else ""

    # 🔍 Search Filter
    if search and search.lower() not in description.lower():
        continue

    with st.container(border=True):
        st.subheader(f"🚨 Incident #{incident_id}")

        

        # Fix for None remarks
        remarks = report[8] if report[8] else ""

        with st.container(border=True):

            st.subheader(f"🚨 Incident #{incident_id}")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**📂 Category:** {category}")
                st.write(f"**📍 Location:** {location}")
                st.write(f"**📅 Date:** {incident_date}")

            with col2:
                st.write(f"**🕒 Time:** {incident_time}")
                st.write(f"**⏰ Reported:** {reported_time}")

            st.write("### 📝 Description")
            st.info(description)

            # Status Display
            if status == "Pending":
                st.error("🟡 Status : Pending")
                st.progress(25)

            elif status == "Viewed":
                st.info("👀 Status : Viewed")
                st.progress(50)

            elif status == "In Progress":
                st.warning("🔵 Status : In Progress")
                st.progress(75)

            elif status == "Resolved":
                st.success("🟢 Status : Resolved")
                st.progress(100)

            st.write("### 💬 Management Remarks")

            if remarks.strip():
                st.success(remarks)
            else:
                st.info("No remarks added yet.")

            st.markdown("---")

else:
    st.info("No reports found.")

st.divider()

st.success("✅ You can track every complaint submitted to the management.")

st.caption("Campus Safety Incident Logger | Student Report Tracking")