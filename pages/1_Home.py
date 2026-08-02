import streamlit as st


st.set_page_config(
    page_title="Campus Safety Incident Logger",
    page_icon="🛡️",
    layout="wide"
)



# ================= CUSTOM CSS =================


st.markdown("""
<style>


/* Background */

.stApp{

background:

linear-gradient(
135deg,
#ecfdf5,
#cffafe,
#f0fdfa
);

}



/* Hero */


.hero{

background:

linear-gradient(
135deg,
#065f46,
#0f766e,
#0891b2
);


padding:60px;

border-radius:35px;

text-align:center;

color:white;

box-shadow:

0 20px 50px rgba(0,0,0,0.25);

}



.hero h1{

font-size:60px;

font-weight:900;

margin-bottom:10px;

}



.hero h3{

font-size:25px;

color:#ccfbf1;

}



.hero p{

font-size:20px;

}




/* Glass Card */


.card{

background:

rgba(255,255,255,0.75);

backdrop-filter:blur(12px);


padding:30px;

border-radius:25px;


box-shadow:

0 10px 30px rgba(0,0,0,0.15);


border-top:

6px solid #0d9488;


text-align:center;


}



/* Stats */


.stat{

background:white;

padding:25px;

border-radius:20px;


box-shadow:

0 8px 20px rgba(0,0,0,.12);


text-align:center;


}



.stat h1{

font-size:45px;

}




.stat h2{

color:#047857;

}




/* Feature */


.feature{


background:

linear-gradient(
135deg,
#ffffff,
#ecfeff
);


padding:25px;


border-radius:22px;


height:190px;


box-shadow:

0 8px 25px rgba(0,0,0,.12);


border-left:

7px solid #14b8a6;


}



.feature h2{

color:#0f766e;

}



/* AI Section */


.ai-box{


background:

linear-gradient(
135deg,
#064e3b,
#0f766e
);


padding:35px;


border-radius:30px;


color:white;


box-shadow:

0 15px 40px rgba(0,0,0,.25);


}



.ai-box h2{

color:#99f6e4;

}




/* Workflow */


.workflow{


background:white;


padding:30px;


border-radius:25px;


font-size:20px;


text-align:center;


box-shadow:

0 10px 25px rgba(0,0,0,.15);


border-left:

8px solid #0891b2;


}




.footer{


text-align:center;


padding:35px;


color:#475569;


}


</style>

""",
unsafe_allow_html=True)




# ================= HERO =================



st.markdown("""
<div class="hero">


<h1>
🛡️ Campus Safety<br>
Incident Logger
</h1>


<h3>
AI Powered Smart Campus Protection System
</h3>


<p>
Protect Students • Report Incidents • Resolve Faster
</p>


</div>

""",
unsafe_allow_html=True)




st.write("")




# ================= STATS =================


st.subheader("📊 System Highlights")



c1,c2,c3,c4 = st.columns(4)



stats=[

("🚨","Incident Reporting"),

("🤖","AI Detection"),

("💾","SQLite Database"),

("📈","Analytics")

]



for col,item in zip(
[c1,c2,c3,c4],
stats
):

    with col:

        st.markdown(f"""

        <div class="stat">


        <h1>{item[0]}</h1>


        <h2>{item[1]}</h2>


        </div>


        """,
        unsafe_allow_html=True)




st.write("")




# ================= ABOUT =================



st.markdown("""
<div class="card">


<h2>
🚀 About The Project
</h2>


<p>

Campus Safety Incident Logger is an AI-powered
web application designed to improve campus security.

Students can report incidents digitally while
administrators can monitor and resolve complaints
through a centralized system.

</p>


</div>

""",
unsafe_allow_html=True)




st.divider()




# ================= FEATURES =================



st.subheader("✨ Key Features")



c1,c2,c3=st.columns(3)



features=[

("🚨 Digital Reporting",
"Quick and secure incident submission"),

("🤖 AI Classification",
"Automatic incident category prediction"),

("👨‍💼 Admin Dashboard",
"Manage and track complaints")

]



for col,item in zip(
[c1,c2,c3],
features
):

    with col:


        st.markdown(f"""

        <div class="feature">


        <h2>{item[0]}</h2>


        <p>{item[1]}</p>


        </div>


        """,
        unsafe_allow_html=True)




st.write("")




# ================= AI =================



st.markdown("""
<div class="ai-box">


<h2>
🤖 Artificial Intelligence Layer
</h2>


<p>

The system uses AI techniques to analyse
incident descriptions, classify safety issues
and generate preventive suggestions.

</p>


</div>

""",
unsafe_allow_html=True)




st.divider()




# ================= WORKFLOW =================



st.subheader("⚙ System Workflow")



st.markdown("""
<div class="workflow">


👨‍🎓 Student Reports Incident

<br>⬇<br>

🚨 Incident Submission

<br>⬇<br>

🤖 AI Processing

<br>⬇<br>

💾 Database Storage

<br>⬇<br>

👨‍💼 Admin Verification

<br>⬇<br>

🛡 Safer Campus


</div>

""",
unsafe_allow_html=True)




st.divider()




# ================= FUTURE =================



st.subheader("🚀 Future Enhancements")



x,y,z=st.columns(3)



for col,text in zip(
[x,y,z],
[
"📱 Mobile Application",
"📍 GPS Tracking",
"🎥 Smart CCTV"
]
):

    with col:

        st.markdown(f"""

        <div class="card">

        <h2>{text}</h2>

        </div>

        """,
        unsafe_allow_html=True)




st.divider()




# ================= FOOTER =================



st.markdown("""
<div class="footer">


<h2>
🛡 Campus Safety Incident Logger
</h2>


<p>
Python | Streamlit | AI/ML | SQLite
</p>


<p>
Artificial Intelligence and Data Science | KIET | JNTUK
</p>


</div>

""",
unsafe_allow_html=True)