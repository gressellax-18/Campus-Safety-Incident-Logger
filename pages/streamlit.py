import streamlit as st


st.set_page_config(
    page_title="Programming Used",
    page_icon="💻",
    layout="wide"
)


# ================= CSS =================

st.markdown("""
<style>

/* Background */

.stApp{

background:
linear-gradient(
135deg,
#f5f3ff,
#ecfeff
);

}


/* Header */

.hero{

background:
linear-gradient(
135deg,
#4f46e5,
#9333ea
);

padding:45px;

border-radius:30px;

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

color:#e0e7ff;

}



/* Section */

.section{

font-size:32px;

font-weight:900;

color:#312e81;

margin-top:25px;

}



/* Cards */


.card{

background:white;

padding:25px;

border-radius:22px;

box-shadow:
0 10px 25px rgba(0,0,0,0.12);

text-align:center;

margin-bottom:20px;

}




.card h2{

color:#4f46e5;

}



/* Python */

.python{

background:
linear-gradient(
135deg,
#fef9c3,
#fde68a
);

padding:25px;

border-radius:20px;

border-left:8px solid #eab308;

}




/* AI */


.ai{

background:
linear-gradient(
135deg,
#dcfce7,
#bbf7d0
);

padding:25px;

border-radius:20px;

border-left:8px solid #16a34a;

}



/* Database */


.database{

background:
linear-gradient(
135deg,
#dbeafe,
#bfdbfe
);

padding:25px;

border-radius:20px;

border-left:8px solid #2563eb;

}



/* Workflow */


.workflow{

background:white;

padding:30px;

border-radius:25px;

box-shadow:
0 10px 25px rgba(0,0,0,.15);

font-size:18px;

line-height:2;

}



/* Footer */


.footer{

text-align:center;

padding:30px;

color:#64748b;

}



</style>

""",
unsafe_allow_html=True)




# ================= HEADER =================


st.markdown("""
<div class="hero">

<h1>💻 Programming & Technologies Used</h1>

<p>
Technology Stack Behind Campus Safety Incident Logger
</p>

</div>

""",
unsafe_allow_html=True)



st.write("")




# ================= OVERVIEW =================


st.markdown(
'<div class="section">📌 Project Overview</div>',
unsafe_allow_html=True
)



st.markdown("""
<div class="card">

<h2>
🚀 Python Based Smart Application
</h2>


<p>

Campus Safety Incident Logger is developed using Python
and Streamlit framework.

The system integrates database management,
AI/ML processing and analytics to create a smart
campus safety platform.

</p>

</div>

""",
unsafe_allow_html=True)



st.divider()




# ================= TECHNOLOGIES =================


st.markdown(
'<div class="section">🛠 Core Technologies</div>',
unsafe_allow_html=True
)



c1,c2,c3=st.columns(3)



with c1:

    st.markdown("""
    <div class="python">

    <h2>🐍 Python</h2>

    <p>
    Main programming language used for
    application logic, AI processing and database operations.
    </p>

    </div>

    """,
    unsafe_allow_html=True)




with c2:

    st.markdown("""
    <div class="database">

    <h2>💾 SQLite</h2>

    <p>
    Database used for storing incidents,
    user reports and management updates.
    </p>

    </div>

    """,
    unsafe_allow_html=True)




with c3:

    st.markdown("""
    <div class="ai">

    <h2>🤖 AI / ML</h2>

    <p>
    Used for incident classification
    and safety recommendations.
    </p>

    </div>

    """,
    unsafe_allow_html=True)



st.divider()




# ================= STREAMLIT =================


st.markdown(
'<div class="section">🚀 Why Streamlit?</div>',
unsafe_allow_html=True
)



features=[

"⚡ Rapid Web Application Development",

"🐍 Direct Python Integration",

"📊 Interactive Dashboard Support",

"🤖 AI Model Integration",

"☁ Easy Cloud Deployment",

"🎨 No Frontend Coding Required"

]



cols=st.columns(3)



for i,item in enumerate(features):

    with cols[i%3]:

        st.markdown(f"""

        <div class="card">

        <h3>{item}</h3>

        </div>

        """,
        unsafe_allow_html=True)




st.divider()




# ================= LIBRARIES =================


st.markdown(
'<div class="section">📚 Python Libraries</div>',
unsafe_allow_html=True
)



l1,l2,l3=st.columns(3)



libraries=[

("⚡ Streamlit",
"Frontend and dashboard development"),

("📊 Pandas",
"Data analysis and processing"),

("🤖 Scikit Learn",
"Machine learning implementation")

]



for col,data in zip(
    [l1,l2,l3],
    libraries
):

    with col:

        st.markdown(f"""

        <div class="card">

        <h2>{data[0]}</h2>

        <p>{data[1]}</p>

        </div>

        """,
        unsafe_allow_html=True)



st.divider()




# ================= MODULES =================


st.markdown(
'<div class="section">📂 Project Modules</div>',
unsafe_allow_html=True
)



modules=[

"🏠 Home",

"📖 About",

"🚨 Report Incident",

"📄 My Reports",

"👨‍💼 Admin Dashboard",

"📊 Analytics",

"🤖 AI Layer",

"🚀 Live Demo"

]



cols=st.columns(4)



for i,m in enumerate(modules):

    with cols[i%4]:

        st.markdown(f"""

        <div class="card">

        <h3>{m}</h3>

        </div>

        """,
        unsafe_allow_html=True)



st.divider()




# ================= WORKFLOW =================


st.markdown(
'<div class="section">⚙ System Workflow</div>',
unsafe_allow_html=True
)



st.markdown("""
<div class="workflow">


👨‍🎓 Student Reports Incident

<br>⬇<br>

🚨 Incident Submission

<br>⬇<br>

🤖 AI Classification

<br>⬇<br>

💾 SQLite Database

<br>⬇<br>

👨‍💼 Admin Verification

<br>⬇<br>

📊 Analytics Dashboard

<br>⬇<br>

🛡 Safer Campus


</div>

""",
unsafe_allow_html=True)



st.divider()




# ================= ADVANTAGES =================


st.markdown(
'<div class="section">🌟 Advantages</div>',
unsafe_allow_html=True
)



a,b=st.columns(2)



with a:

    st.success("✔ User Friendly Interface")

    st.success("✔ Secure Database")

    st.success("✔ Fast Processing")



with b:

    st.info("✔ AI Ready Architecture")

    st.info("✔ Easy Deployment")

    st.info("✔ Future Scalable")




st.divider()




# ================= FOOTER =================


st.markdown("""
<div class="footer">


<h2>
🎉 Campus Safety Incident Logger
</h2>


<p>
Developed using Python | Streamlit | AI/ML | SQLite
</p>


<p>
Artificial Intelligence and Data Science | KIET | JNTUK
</p>


</div>

""",
unsafe_allow_html=True)