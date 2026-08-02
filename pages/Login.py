import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="KIET Campus Safety - Login",
    page_icon="🛡️",
    layout="centered"
)

# 2. Custom CSS for UI Design and Logo Text Styling
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #f4f7fc;
    }
    
    /* Header & Titles Styling */
    .header-container {
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Pure CSS/HTML Logo Styling */
    .logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-bottom: 8px;
    }
    
    .vertical-brand-text {
        color: #d32f2f; /* Red */
        font-size: 11px;
        font-weight: 800;
        line-height: 1.1;
        letter-spacing: 1px;
        text-align: center;
        border-right: 2px solid #000000;
        padding-right: 6px;
    }
    
    .main-logo-text {
        font-size: 52px;
        font-weight: 900;
        letter-spacing: 1px;
        margin: 0;
        line-height: 1;
        font-family: Arial, sans-serif;
    }
    
    .navy-text {
        color: #1a237e; /* Dark Blue */
    }
    
    .red-text {
        color: #d32f2f; /* Red */
    }

    .sub-heading {
        color: #1a237e;
        font-size: 15px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-top: 6px;
    }
    
    .tagline {
        color: #557097;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 1.5px;
        margin-top: 8px;
    }

    /* Card Styling */
    div[data-testid="stVerticalBlock"] > div:has(div.login-card) {
        background: #ffffff;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.08);
    }
    
    .login-header {
        text-align: center;
        color: #1a237e;
        font-weight: 700;
        font-size: 22px;
        margin-bottom: 15px;
    }

    /* Primary Login Button */
    div.stButton > button {
        width: 100%;
        background-color: #1a237e !important;
        color: white !important;
        border-radius: 8px !important;
        height: 48px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        border: none !important;
    }
    div.stButton > button:hover {
        background-color: #0d1b60 !important;
    }
    /* Hide the entire sidebar */
[data-testid="stSidebar"] {
    display: none !important;
}

/* Hide the collapse/expand sidebar arrow button at top left */
[data-testid="collapsedControl"] {
    display: none !important;
}

/* Allow the login card to center cleanly on the screen */
.stApp {
    margin: 0 auto;
}
    
    </style>
""", unsafe_allow_html=True)

# 3. Header Section with Styled HTML Text Logo
st.markdown("""
    <div class="header-container">
        <div class="logo-container">
            <div class="vertical-brand-text">K<br>I<br>E<br>T</div>
            <h1 class="main-logo-text">
                <span class="navy-text">K</span><span class="red-text">I</span><span class="navy-text">ET</span>
            </h1>
        </div>
        <div class="sub-heading">KAKINADA INSTITUTE OF ENGINEERING & TECHNOLOGY</div>
        <div class="tagline">CAMPUS SAFETY INCIDENT LOGGER</div>
    </div>
""", unsafe_allow_html=True)

# 4. Login Form Card Layout
col1, col2, col3 = st.columns([0.1, 0.8, 0.1])

with col2:
    with st.container():
        st.markdown('<div class="login-card login-header">LOGIN</div>', unsafe_allow_html=True)
        
        # User Role Selection
        role = st.radio(
            label="Select Role",
            options=["Parent", "Student"],
            horizontal=True,
            index=1,
            label_visibility="collapsed"
        )
        
        # Input Fields
        username = st.text_input("Username", placeholder="Username", label_visibility="collapsed")
        password = st.text_input("Password", type="password", placeholder="Password", label_visibility="collapsed")
        
        st.write("") # Spacing
        
        # Submit Button
        if st.button("LOGIN"):
            if username and password:
                st.success("Login successful!")
                st.switch_page("pages/1_Home.py")
            else:
                st.error("Please enter both username and password.")