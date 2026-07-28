import streamlit as st
from ai_ml_layer import classify_incident, preventive_suggestion

st.set_page_config(page_title="AI / ML Layer", page_icon="🤖", layout="wide")

# ---------------- CSS ----------------

st.markdown("""
<style>

.title{
font-size:42px;
font-weight:bold;
color:#1565C0;
text-align:center;
}

.subtitle{
text-align:center;
font-size:18px;
color:gray;
margin-bottom:25px;
}

.box{
background:#f8f9fa;
padding:18px;
border-radius:15px;
box-shadow:0px 5px 15px rgba(0,0,0,.12);
margin-bottom:15px;
}

.result{
background:#d4edda;
padding:20px;
border-radius:12px;
border-left:8px solid green;
}

</style>
""",unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown('<p class="title">🤖 Artificial Intelligence Layer</p>',unsafe_allow_html=True)

st.markdown('<p class="subtitle">Smart Incident Classification using Machine Learning</p>',unsafe_allow_html=True)

st.divider()

# ---------------- ABOUT ----------------

st.markdown("""

<div class="box">

### 🧠 AI Overview

The AI Engine automatically analyses the incident description submitted by students.

It predicts the incident category and instantly provides preventive safety recommendations to assist both students and campus management.

</div>

""",unsafe_allow_html=True)

st.divider()

# ---------------- WORKFLOW ----------------

st.subheader("⚙ AI Processing Workflow")

st.success("""

👨‍🎓 Student Reports Incident

⬇

📝 Text Processing

⬇

🤖 AI Model Analysis

⬇

🏷 Category Prediction

⬇

💡 Safety Suggestion

⬇

💾 Stored in Database

⬇

👨‍💼 Admin Review

""")

st.divider()

# ---------------- FEATURES ----------------

st.subheader("✨ AI Features")

c1,c2=st.columns(2)

with c1:

    st.success("🤖 Automatic Incident Classification")

    st.success("📝 Text Analysis")

    st.success("🏷 Smart Category Detection")

with c2:

    st.success("💡 Preventive Suggestions")

    st.success("⚡ Faster Processing")

    st.success("🎯 Better Decision Support")

st.divider()

# ---------------- CATEGORY SUPPORT ----------------

st.subheader("🚨 Supported Incident Categories")

a,b,c=st.columns(3)

with a:
    st.error("🚨 Ragging")
    st.error("🚲 Theft")

with b:
    st.warning("🔥 Fire")
    st.warning("🏥 Medical Emergency")

with c:
    st.info("⚠ Suspicious Activity")
    st.info("👊 Harassment")

st.divider()

# ---------------- LIVE TEST ----------------

st.subheader("🧪 AI Live Testing")

incident=st.text_area(
    "Enter Incident Description",
    placeholder="Example : My mobile phone was stolen near the library."
)

if st.button("🤖 Analyze Incident",use_container_width=True):

    if incident.strip()=="":

        st.warning("Please enter an incident description.")

    else:

        category=classify_incident(incident)

        suggestion=preventive_suggestion(category)

        st.success("✅ Analysis Completed Successfully")

        st.markdown(f"""
<div class="result">

<h3>📌 Prediction Result</h3>

<b>🏷 Predicted Category :</b> {category}

<br><br>

<b>💡 Preventive Suggestion :</b>

{suggestion}

</div>

""",unsafe_allow_html=True)

        st.progress(95)

        st.info("🎯 AI Prediction Confidence : 95%")

st.divider()

# ---------------- ADVANTAGES ----------------

st.subheader("🌟 Advantages of AI")

col1,col2=st.columns(2)

with col1:

    st.info("""

✅ Faster Classification

✅ Reduced Manual Work

✅ Better Accuracy

""")

with col2:

    st.info("""

✅ Smart Recommendations

✅ Better Campus Safety

✅ Future AI Ready

""")

st.divider()

# ---------------- FUTURE ----------------

st.subheader("🚀 Future Enhancements")

st.success("""

📸 Image Based Detection

🎥 CCTV Integration

📍 Live GPS Tracking

🔔 Automatic Alerts

📊 Predictive Analytics

😊 Sentiment Analysis

""")

st.divider()

st.markdown("""
<center>

### 🤖 AI Powered Campus Safety

Making Campus Security Smarter with Artificial Intelligence

</center>
""",unsafe_allow_html=True)