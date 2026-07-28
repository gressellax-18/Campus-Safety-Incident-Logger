import streamlit as st
from ai_ml_layer import classify_incident, preventive_suggestion


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Live Demo | Campus Safety",
    page_icon="🚀",
    layout="wide"
)


# ---------------- CSS ----------------

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:800;
    color:#0D47A1;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:#555;
}

.card{
    background:white;
    padding:22px;
    border-radius:18px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.12);
    border-left:6px solid #1565C0;
}

.ai-card{
    background:#E8F5E9;
    padding:25px;
    border-radius:18px;
    border-left:8px solid green;
}

.cctv-card{
    background:#E3F2FD;
    padding:25px;
    border-radius:18px;
    border-left:8px solid #0277BD;
}

.workflow{
    background:#F5F7FA;
    padding:20px;
    border-radius:15px;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)



# ---------------- HEADER ----------------


st.markdown(
    '<div class="main-title">🚀 AI Powered Live Demonstration</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="subtitle">'
    'Campus Safety Incident Logger - Intelligent Monitoring System'
    '</div>',
    unsafe_allow_html=True
)


st.divider()



# ---------------- INTRO ----------------


st.markdown("""
<div class="card">

<h2>🎯 Live Demo Purpose</h2>

This demonstration shows how Artificial Intelligence helps
campus authorities in:

<br><br>

✔ Automatic incident classification

<br>

✔ Safety recommendation generation

<br>

✔ CCTV based threat monitoring

<br>

✔ Faster emergency response

</div>

""", unsafe_allow_html=True)



st.divider()



# ==================================================
# AI INCIDENT ANALYSIS
# ==================================================


st.subheader("📝 Student Incident Reporting")


incident = st.text_area(
    "Describe Incident",
    height=120,
    placeholder=
    "Example: My mobile phone was stolen near the library."
)



if st.button(
    "🤖 Analyze Incident",
    use_container_width=True
):

    if incident.strip()=="":
        st.warning(
            "Please enter incident description."
        )

    else:

        with st.spinner(
            "AI is analyzing the complaint..."
        ):


            category = classify_incident(incident)

            suggestion = preventive_suggestion(category)



        st.success(
            "AI Analysis Completed Successfully"
        )


        st.divider()


        st.subheader(
            "📊 AI Analysis Result"
        )


        c1,c2,c3 = st.columns(3)


        with c1:

            st.metric(
                "🏷 Category",
                category
            )


        with c2:

            st.metric(
                "⚡ Priority",
                "High"
            )


        with c3:

            st.metric(
                "🤖 Confidence",
                "95%"
            )


        st.progress(95)



        st.divider()



        st.markdown(
        f"""

<div class="ai-card">

<h3>💡 AI Safety Recommendation</h3>

<p>{suggestion}</p>

</div>

        """,
        unsafe_allow_html=True
        )



# ==================================================
# CCTV SURVEILLANCE MODULE
# ==================================================


        st.markdown(
        f"""

<div class="ai-card">

<h3>💡 AI Safety Recommendation</h3>

<p>{suggestion}</p>

</div>

        """,
        unsafe_allow_html=True
        )


# ==============================
# 📹 CCTV MODULE START HERE
# ==============================


st.divider()

st.subheader("📹 AI Based CCTV Surveillance System")


st.markdown("""
<div class="cctv-card">

<h3>👁 Smart Campus Vision</h3>

AI monitors CCTV feeds and detects suspicious activities.

</div>

""", unsafe_allow_html=True)



camera = st.selectbox(
    "Select CCTV Camera",
    [
        "Main Gate Camera",
        "Library Camera",
        "Parking Area Camera",
        "Hostel Corridor Camera",
        "Laboratory Camera"
    ]
)


st.info(f"📡 Monitoring : {camera}")


event = st.selectbox(
    "Simulate CCTV Event",
    [
        "Normal Activity",
        "Suspicious Person Detected",
        "Unauthorized Entry",
        "Fire / Smoke Detection",
        "Student Emergency"
    ]
)


if st.button("🔍 Analyze CCTV Feed"):

    if event=="Normal Activity":

        st.success(
        "✅ Normal Activity Detected - No Risk Found"
        )

    elif event=="Suspicious Person Detected":

        st.warning(
        "⚠ Suspicious Person Detected. Alert Security Team."
        )

    elif event=="Unauthorized Entry":

        st.error(
        "🚨 Unauthorized Entry Detected."
        )

    elif event=="Fire / Smoke Detection":

        st.error(
        "🔥 Fire Risk Detected. Emergency Response Activated."
        )

    else:

        st.warning(
        "🏥 Student Emergency Detected."
        )


# ==============================
# 📹 CCTV MODULE END
# ==============================


        st.markdown(
        f"""

<div class="ai-card">

<h3>💡 AI Safety Recommendation</h3>

<p>{suggestion}</p>

</div>

        """,
        unsafe_allow_html=True
        )


# ==============================
# 📹 CCTV MODULE START HERE
# ==============================


st.divider()

st.subheader("📹 AI Based CCTV Surveillance System")


st.markdown("""
<div class="cctv-card">

<h3>👁 Smart Campus Vision</h3>

AI monitors CCTV feeds and detects suspicious activities.

</div>

""", unsafe_allow_html=True)



camera = st.selectbox(
    "Select CCTV Camera",
    [
        "Main Gate Camera",
        "Library Camera",
        "Parking Area Camera",
        "Hostel Corridor Camera",
        "Laboratory Camera"
    ]
)


st.info(f"📡 Monitoring : {camera}")


event = st.selectbox(
    "Simulate CCTV Event",
    [
        "Normal Activity",
        "Suspicious Person Detected",
        "Unauthorized Entry",
        "Fire / Smoke Detection",
        "Student Emergency"
    ]
)


if st.button("🔍 Analyze CCTV Feed"):

    if event=="Normal Activity":

        st.success(
        "✅ Normal Activity Detected - No Risk Found"
        )

    elif event=="Suspicious Person Detected":

        st.warning(
        "⚠ Suspicious Person Detected. Alert Security Team."
        )

    elif event=="Unauthorized Entry":

        st.error(
        "🚨 Unauthorized Entry Detected."
        )

    elif event=="Fire / Smoke Detection":

        st.error(
        "🔥 Fire Risk Detected. Emergency Response Activated."
        )

    else:

        st.warning(
        "🏥 Student Emergency Detected."
        )


# ==============================
# 📹 CCTV MODULE END
# ==============================

        st.markdown(
        f"""

<div class="ai-card">

<h3>💡 AI Safety Recommendation</h3>

<p>{suggestion}</p>

</div>

        """,
        unsafe_allow_html=True
        )


# ==============================
# 📹 CCTV MODULE START HERE
# ==============================


st.divider()

st.subheader("📹 AI Based CCTV Surveillance System")


st.markdown("""
<div class="cctv-card">

<h3>👁 Smart Campus Vision</h3>

AI monitors CCTV feeds and detects suspicious activities.

</div>

""", unsafe_allow_html=True)



camera = st.selectbox(
    "Select CCTV Camera",
    [
        "Main Gate Camera",
        "Library Camera",
        "Parking Area Camera",
        "Hostel Corridor Camera",
        "Laboratory Camera"
    ]
)


st.info(f"📡 Monitoring : {camera}")


event = st.selectbox(
    "Simulate CCTV Event",
    [
        "Normal Activity",
        "Suspicious Person Detected",
        "Unauthorized Entry",
        "Fire / Smoke Detection",
        "Student Emergency"
    ]
)


if st.button("🔍 Analyze CCTV Feed"):

    if event=="Normal Activity":

        st.success(
        "✅ Normal Activity Detected - No Risk Found"
        )

    elif event=="Suspicious Person Detected":

        st.warning(
        "⚠ Suspicious Person Detected. Alert Security Team."
        )

    elif event=="Unauthorized Entry":

        st.error(
        "🚨 Unauthorized Entry Detected."
        )

    elif event=="Fire / Smoke Detection":

        st.error(
        "🔥 Fire Risk Detected. Emergency Response Activated."
        )

    else:

        st.warning(
        "🏥 Student Emergency Detected."
        )


# ==============================
# 📹 CCTV MODULE END
# ==============================



# ---------------- SAMPLE DEMO ----------------

st.divider()

st.subheader("📌 Sample Incident Examples")
st.divider()


st.subheader(
    "📹 AI Based CCTV Surveillance System"
)



st.markdown("""
<div class="cctv-card">

<h3>👁 Smart Campus Vision</h3>

AI monitors CCTV feeds and detects
suspicious activities, emergencies and safety threats.

</div>

""",
unsafe_allow_html=True)



st.divider()



cam1,cam2,cam3 = st.columns(3)


with cam1:

    st.metric(
        "📹 Active Cameras",
        "24"
    )


with cam2:

    st.metric(
        "👥 People Detected",
        "156"
    )


with cam3:

    st.metric(
        "🚨 Alerts",
        "3"
    )



st.divider()



camera = st.selectbox(
    "Select CCTV Camera",

    [
        "Main Gate Camera",
        "Library Camera",
        "Parking Area Camera",
        "Hostel Corridor Camera",
        "Laboratory Camera"
    ]
)


st.info(
    f"📡 Monitoring : {camera}"
)



event = st.selectbox(
    "Simulate CCTV Event",

    [
        "Normal Activity",
        "Suspicious Person Detected",
        "Unauthorized Entry",
        "Fire / Smoke Detection",
        "Student Emergency"
    ]
)



if st.button(
    "🔍 Analyze CCTV Feed",
    use_container_width=True
):


    if event=="Normal Activity":

        st.success(
        """
        ✅ Normal Activity Detected

        AI Status:
        No security risk identified.
        """
        )


    elif event=="Suspicious Person Detected":

        st.warning(
        """
        ⚠ Suspicious Activity Detected

        AI Observation:
        Unusual movement pattern found.

        Action:
        Inform security team.
        """
        )


    elif event=="Unauthorized Entry":

        st.error(
        """
        🚨 Unauthorized Entry Alert

        AI Observation:
        Restricted area access detected.

        Action:
        Verify person identity.
        """
        )


    elif event=="Fire / Smoke Detection":

        st.error(
        """
        🔥 Fire Hazard Detected

        AI Observation:
        Smoke pattern detected.

        Action:
        Activate emergency response.
        """
        )


    else:

        st.warning(
        """
        🏥 Student Emergency Detected

        AI Observation:
        Possible health emergency.

        Action:
        Contact medical support.
        """
        )



# ==================================================
# SAMPLE INCIDENTS
# ==================================================


st.divider()


st.subheader(
    "📌 Sample Incident Examples"
)


samples=[

"Mobile stolen near library",

"Fire detected in laboratory",

"Student harassment complaint",

"Unknown person near gate",

"Student injured during sports"

]


cols=st.columns(5)


for i,s in enumerate(samples):

    with cols[i]:

        st.info(s)



# ==================================================
# AI WORKFLOW
# ==================================================


st.divider()


st.subheader(
    "⚙ Complete AI Workflow"
)



st.markdown("""
<div class="workflow">


👨‍🎓 Student Reports Incident

<br>⬇<br>

📝 NLP Text Processing

<br>⬇<br>

🤖 AI Classification Model

<br>⬇<br>

🏷 Category Prediction

<br>⬇<br>

📹 CCTV Monitoring

<br>⬇<br>

🚨 Threat Detection

<br>⬇<br>

👮 Security Response

<br>⬇<br>

🛡 Safer Campus Environment


</div>

""",
unsafe_allow_html=True)



# ==================================================
# FEATURES
# ==================================================


st.divider()


st.subheader(
    "✨ System Capabilities"
)



a,b,c = st.columns(3)


with a:

    st.success(
        "🧠 NLP Based Analysis"
    )

    st.success(
        "⚡ Instant Prediction"
    )


with b:

    st.success(
        "📹 CCTV Monitoring"
    )

    st.success(
        "🚨 Alert Generation"
    )


with c:

    st.success(
        "💡 Safety Suggestions"
    )

    st.success(
        "🔒 Campus Protection"
    )



st.divider()



st.success(
    "🎉 AI Live Demonstration Completed Successfully!"
)


st.caption(
    "Campus Safety Incident Logger | AI Powered Smart Campus Solution"
)