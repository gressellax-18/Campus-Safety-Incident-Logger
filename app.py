import streamlit as st

st.set_page_config(
    page_title="Campus Safety Incident Logger",
    page_icon="🛡️",
    layout="wide"
)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:

   st.switch_page("pages/login.py")

else:

    if st.session_state.role == "Student":
        st.switch_page("pages/1_Home.py")

    elif st.session_state.role == "Admin":
        st.switch_page("pages/Admin_Dashboard.py")
        