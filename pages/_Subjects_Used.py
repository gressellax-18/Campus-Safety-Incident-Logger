import streamlit as st


st.set_page_config(
    page_title="Subjects Used",
    page_icon="📚",
    layout="wide"
)



# ================= CSS =================


st.markdown("""
<style>


.stApp{

background:
linear-gradient(
135deg,
#ecfdf5,
#eff6ff
);

}



/* Header */


.hero{

background:
linear-gradient(
135deg,
#047857,
#0ea5e9
);

padding:45px;

border-radius:30px;

text-align:center;

color:white;

box-shadow:
0 15px 35px rgba(0,0,0,.25);

}


.hero h1{

font-size:48px;

font-weight:900;

}



.hero p{

font-size:20px;

color:#d1fae5;

}




/* Section */


.section{

font-size:32px;

font-weight:900;

color:#065f46;

margin-top:25px;

}




/* Cards */


.card{

background:white;

padding:25px;

border-radius:22px;

box-shadow:
0 10px 25px rgba(0,0,0,.12);

margin-bottom:20px;

}




.card h2{

color:#047857;

}




/* Subject */


.subject1{

background:
linear-gradient(
135deg,
#dcfce7,
#bbf7d0
);

border-left:8px solid #16a34a;

padding:25px;

border-radius:20px;

}



.subject2{

background:
linear-gradient(
135deg,
#dbeafe,
#bfdbfe
);

border-left:8px solid #2563eb;

padding:25px;

border-radius:20px;

}



.subject3{

background:
linear-gradient(
135deg,
#fef3c7,
#fde68a
);

border-left:8px solid #eab308;

padding:25px;

border-radius:20px;

}



/* Topic */

.topic{

background:white;

padding:18px;

border-radius:15px;

box-shadow:
0 5px 15px rgba(0,0,0,.1);

text-align:center;

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

<h1>📚 Subjects Used</h1>

<p>
Academic Concepts Integrated into Campus Safety Incident Logger
</p>

</div>

""",
unsafe_allow_html=True)



st.write("")



# ================= INTRO =================


st.markdown(
'<div class="section">🎓 Subject Integration Overview</div>',
unsafe_allow_html=True
)



st.markdown("""
<div class="card">


<h2>
📌 Academic Implementation
</h2>


<p>

This mini project combines concepts from different
R23 curriculum subjects.

The knowledge gained from programming,
software tools and social awareness subjects
helped in developing this smart campus safety system.

</p>


</div>

""",
unsafe_allow_html=True)




st.divider()




# ================= SUBJECT CARDS =================



st.markdown(
'<div class="section">📖 Integrated Subjects</div>',
unsafe_allow_html=True
)



c1,c2,c3 = st.columns(3)




with c1:


    st.markdown("""
    <div class="subject1">

    <h2>
    🐍 Programming for Problem Solving
    </h2>


    <p>

    <b>Contribution:</b>

    <br><br>

    ✔ Python Programming

    <br>

    ✔ Logic Building

    <br>

    ✔ Problem Solving

    <br>

    ✔ File Handling

    <br>

    ✔ Data Processing


    </p>


    </div>

    """,
    unsafe_allow_html=True)





with c2:


    st.markdown("""
    <div class="subject2">

    <h2>
    💻 IT Workshop
    </h2>


    <p>

    <b>Contribution:</b>

    <br><br>

    ✔ Software Tools

    <br>

    ✔ Application Development

    <br>

    ✔ Technical Implementation

    <br>

    ✔ Database Usage


    </p>


    </div>

    """,
    unsafe_allow_html=True)





with c3:


    st.markdown("""
    <div class="subject3">

    <h2>
    🤝 NSS / Community Service
    </h2>


    <p>

    <b>Contribution:</b>

    <br><br>

    ✔ Social Awareness

    <br>

    ✔ Campus Safety

    <br>

    ✔ Community Responsibility

    <br>

    ✔ Problem Identification


    </p>


    </div>

    """,
    unsafe_allow_html=True)






st.divider()




# ================= TOPICS =================


st.markdown(
'<div class="section">📌 Topics Applied</div>',
unsafe_allow_html=True
)



topics=[

"🐍 Python Programming",

"📂 File Handling",

"🌐 Internet Tools",

"💾 Database Management",

"📊 Data Processing",

"🧠 Problem Solving",

"🤝 Social Awareness",

"🛡 Safety Management"

]



cols=st.columns(4)



for i,topic in enumerate(topics):

    with cols[i%4]:

        st.markdown(f"""

        <div class="topic">

        <h3>
        ✅ {topic}
        </h3>

        </div>


        """,
        unsafe_allow_html=True)





st.divider()




# ================= R23 ALIGNMENT =================



st.markdown(
'<div class="section">🔗 R23 Curriculum Alignment</div>',
unsafe_allow_html=True
)




st.markdown("""
<div class="card">


<h2>
📘 Semester-I: Programming Concepts
</h2>


✔ Python Programming

<br>

✔ File Handling

<br>

✔ Data Processing

<br>

✔ Problem Solving


<br><br>


<h2>
📗 Semester-II: NSS / Community Service
</h2>


✔ Social Responsibility

<br>

✔ Safety Awareness

<br>

✔ Community Problem Identification


</div>

""",
unsafe_allow_html=True)





st.divider()




# ================= FOOTER =================


st.success(
"🎉 Subjects successfully integrated into Campus Safety Incident Logger."
)



st.markdown("""
<div class="footer">

<h2>
📚 Campus Safety Incident Logger
</h2>

<p>
Academic Integration | R23 Curriculum | KIET | JNTUK
</p>

</div>

""",
unsafe_allow_html=True)