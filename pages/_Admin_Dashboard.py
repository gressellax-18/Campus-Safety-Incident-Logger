import streamlit as st
from database import create_table, get_incidents

create_table()

st.title("Admin Dashboard")

reports = get_incidents()

st.subheader("All Reported Incidents")

if reports:
    for report in reports:
        st.write(f"ID: {report[0]}")
        st.write(f"Description: {report[1]}")
        st.write(f"Category: {report[2]}")
        st.write("---")
else:
    st.info("No incidents reported yet.")