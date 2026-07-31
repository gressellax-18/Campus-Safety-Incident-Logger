import streamlit as st

from auth import register_user, create_user_table


st.set_page_config(
    page_title="Register",
    page_icon="📝"
)


# Create user table automatically

create_user_table()


st.title("📝 Create New Account")


st.write(
    "Register for Campus Safety Logger"
)



# User Inputs

name = st.text_input(
    "Full Name"
)


email = st.text_input(
    "Email Address"
)


password = st.text_input(
    "Password",
    type="password"
)


role = st.selectbox(
    "Select Role",
    [
        "Student",
        "Admin"
    ]
)



# Register Button

if st.button("Register"):


    if name and email and password:


        result = register_user(
            name,
            email,
            password,
            role
        )


        if result:

            st.success(
                "Registration Successful! Please Login."
            )


        else:

            st.error(
                "Email already registered."
            )


    else:

        st.warning(
            "Please fill all details."
        )