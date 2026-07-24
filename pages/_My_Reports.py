import streamlit as st
from database import create_table, get_incidents

# Create table if it doesn't exist
create_table()

st.title("My Reports")

reports = get_incidents()

if reports:
    for report in reports:
        st.write(f"ID: {report[0]}")
        st.write(f"Description: {report[1]}")
        st.write(f"Category: {report[2]}")
        st.write("---")
else:
    st.info("No reports found.")