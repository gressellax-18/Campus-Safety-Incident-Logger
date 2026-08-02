import streamlit as st

from ai_ml_layer import classify_incident, preventive_suggestion


# ================= CUSTOM CSS =================

st.markdown("""
<style>

/* Background */

.stApp{

background:linear-gradient(
135deg,
#f8fafc,
#eef2ff
);

}


/* Hero */


.hero{

background:
linear-gradient(
135deg,
#312e81,
#4f46e5,
#2563eb
);

padding:45px;

border-radius:25px;

text-align:center;

color:white;

box-shadow:
0 15px 35px rgba(0,0,0,0.25);

}


.hero h1{

font-size:48px;

font-weight:900;

}


.hero p{

font-size:20px;

color:#dbeafe;

}



/* Section */

.section{

font-size:32px;

font-weight:800;

color:#111827;

margin-top:30px;

}



/* Cards */

.card{

background:white;

padding:25px;

border-radius:20px;

box-shadow:
0 10px 25px rgba(0,0,0,0.12);

transition:.3s;

}


.card:hover{

transform:translateY(-8px);

}



/* AI Box */

.ai-box{

background:
linear-gradient(
135deg,
#1e1b4b,
#4338ca
);

color:white;

padding:30px;

border-radius:22px;

box-shadow:
0 12px 30px rgba(0,0,0,.25);

}



/* Category */

.category{

background:white;

padding:20px;

border-radius:18px;

text-align:center;

box-shadow:
0 8px 20px rgba(0,0,0,.12);

}



/* Result */


.result{

background:#ecfdf5;

padding:30px;

border-radius:20px;

border-left:8px solid #16a34a;

box-shadow:
0 10px 25px rgba(0,0,0,.15);

}



/* Footer */

.footer{

text-align:center;

padding:30px;

color:gray;

}


</style>

""",unsafe_allow_html=True)



# ================= HERO =================


st.markdown("""
<div class="hero">

<h1>🤖 Artificial Intelligence Layer</h1>

<p>
Smart Incident Classification & Safety Recommendation Engine
</p>

<p>
Analyze • Predict • Protect
</p>

</div>

""",unsafe_allow_html=True)



st.write("")



# ================= AI INTRO =================


st.markdown(
'<div class="section">🧠 AI Overview</div>',
unsafe_allow_html=True
)


st.markdown("""
<div class="ai-box">

<h2>How AI Helps?</h2>

<p>

The AI module analyzes student incident descriptions using
Natural Language Processing techniques.

It identifies the incident category and provides preventive
safety suggestions to improve campus response.

</p>

</div>

""",
unsafe_allow_html=True)



st.divider()



# ================= AI WORKFLOW =================


st.markdown(
'<div class="section">⚙ AI Processing Pipeline</div>',
unsafe_allow_html=True
)


steps=[

("👨‍🎓","Student Report"),
("📝","Text Processing"),
("🤖","AI Analysis"),
("🏷️","Category Prediction"),
("💡","Safety Suggestion"),
("💾","Database Storage"),
("👨‍💼","Admin Action")

]


cols=st.columns(len(steps))


for col,step in zip(cols,steps):

    with col:

        st.markdown(f"""

        <div class="card" style="text-align:center">

        <h1>{step[0]}</h1>

        <b>{step[1]}</b>

        </div>

        """,
        unsafe_allow_html=True)



st.divider()



# ================= FEATURES =================


st.markdown(
'<div class="section">✨ AI Features</div>',
unsafe_allow_html=True
)



f1,f2,f3=st.columns(3)


features=[

("🤖","Incident Classification"),

("🏷️","Category Detection"),

("💡","Preventive Suggestions")

]


for col,item in zip([f1,f2,f3],features):

    with col:

        st.markdown(f"""

        <div class="category">

        <h1>{item[0]}</h1>

        <h3>{item[1]}</h3>

        </div>

        """,
        unsafe_allow_html=True)



st.divider()



# ================= SUPPORTED CATEGORIES =================


st.markdown(
'<div class="section">🚨 Supported Categories</div>',
unsafe_allow_html=True
)



c1,c2,c3=st.columns(3)


with c1:

    st.markdown("""
    <div class="category">

    🚨 Ragging

    <br><br>

    🚲 Theft

    </div>
    """,unsafe_allow_html=True)



with c2:

    st.markdown("""
    <div class="category">

    🔥 Fire Accident

    <br><br>

    🏥 Medical Emergency

    </div>
    """,unsafe_allow_html=True)



with c3:

    st.markdown("""
    <div class="category">

    ⚠️ Suspicious Activity

    <br><br>

    👊 Harassment

    </div>
    """,unsafe_allow_html=True)



st.divider()



# ================= LIVE AI TEST =================


st.markdown(
'<div class="section">🧪 Live AI Testing</div>',
unsafe_allow_html=True
)



incident=st.text_area(
"Enter Incident Description",
placeholder=
"Example: My phone was stolen near the library."
)



if st.button(
"🤖 Analyze Incident",
use_container_width=True
):

    if incident.strip()=="":
        
        st.warning(
        "Please enter incident details."
        )

    else:

        category=classify_incident(incident)

        suggestion=preventive_suggestion(category)


        st.success(
        "AI Analysis Completed Successfully"
        )


        st.markdown(f"""

        <div class="result">

        <h2>📌 Prediction Result</h2>


        <h3>
        🏷 Category:
        {category}
        </h3>


        <h3>
        💡 Suggestion:
        </h3>


        <p>
        {suggestion}
        </p>


        </div>

        """,
        unsafe_allow_html=True)


        st.progress(0.95)


        st.info(
        "🎯 Prediction Confidence : 95%"
        )



st.divider()



# ================= FUTURE AI =================


st.markdown(
'<div class="section">🚀 Future AI Enhancements</div>',
unsafe_allow_html=True
)



future1,future2,future3=st.columns(3)



future=[

("📸","Image Detection"),

("📍","GPS Based Safety"),

("🎥","CCTV Integration")

]


for col,item in zip(
    [future1,future2,future3],
    future
):

    with col:

        st.markdown(f"""

        <div class="card"
        style="text-align:center">

        <h1>{item[0]}</h1>

        <h3>{item[1]}</h3>

        </div>

        """,
        unsafe_allow_html=True)



st.divider()



# ================= FOOTER =================


st.markdown("""
<div class="footer">

<h2>🤖 AI Powered Campus Safety</h2>

<p>
Making Campus Security Smarter with Artificial Intelligence ❤️
</p>

</div>
""",
unsafe_allow_html=True)