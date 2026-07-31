import streamlit as st

from auth import login_user


st.set_page_config(
    page_title="Login",
    page_icon="🔐"
)


st.title("🔐 Campus Safety Logger Login")


st.write(
    "Login to access your dashboard"
)


# Input fields

email = st.text_input(
    "Email Address"
)


password = st.text_input(
    "Password",
    type="password"
)



# Login Button

if st.button("Login"):


    if email and password:


        user = login_user(
            email,
            password
        )


        if user:


            st.success(
                "Login Successful!"
            )


            st.session_state["logged_in"] = True

            st.session_state["username"] = user[0]

            st.session_state["role"] = user[1]


            st.write(
                "Welcome:",
                user[0]
            )


            st.write(
                "Role:",
                user[1]
            )


            # Redirect message

            if user[1] == "Student":

                st.info(
                    "Go to Report Incident / My Reports"
                )


            elif user[1] == "Admin":

                st.info(
                    "Go to Admin Dashboard"
                )



        else:

            st.error(
                "Invalid Email or Password"
            )


    else:

        st.warning(
            "Please enter all details"
        )