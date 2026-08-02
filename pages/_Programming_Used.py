import streamlit as st


st.set_page_config(
    page_title="Programming Used",
    page_icon="💻",
    layout="wide"
)



# ================= CSS =================


st.markdown("""
<style>


.stApp{

background:

linear-gradient(
135deg,
#020617,
#0f172a,
#134e4a
);

color:white;

}



/* HEADER */


.hero{


background:

linear-gradient(
135deg,
#059669,
#06b6d4
);


padding:50px;


border-radius:30px;


text-align:center;


box-shadow:

0 15px 40px rgba(6,182,212,.35);


}


.hero h1{

font-size:50px;

font-weight:900;

color:white;

}


.hero p{

font-size:20px;

color:#d1fae5;

}




/* TECH CARD */


.tech-card{


background:

rgba(255,255,255,0.12);


padding:25px;


border-radius:22px;


border:

1px solid rgba(255,255,255,.2);


box-shadow:

0 10px 25px rgba(0,0,0,.4);


height:180px;


}



.tech-card h2{

color:#5eead4;

}




/* CODE BOX */


.code-box{


background:#000;


padding:25px;


border-radius:20px;


border-left:

7px solid #22c55e;


font-family:monospace;


color:#86efac;


}




/* MODULE */


.module{


background:

linear-gradient(
135deg,
#1e293b,
#334155
);


padding:20px;


border-radius:18px;


border-left:

6px solid #38bdf8;


}



.footer{


text-align:center;

padding:40px;

color:#94a3b8;

}


</style>

""",
unsafe_allow_html=True)





# ================= HEADER =================



st.markdown("""
<div class="hero">


<h1>
💻 Programming & Technologies Used
</h1>


<p>
Software tools and programming concepts used in Campus Safety Incident Logger
</p>


</div>

""",
unsafe_allow_html=True)



st.write("")





# ================= OVERVIEW =================



st.markdown("""
<div class="code-box">


>>> Project : Campus Safety Incident Logger

>>> Language : Python

>>> Framework : Streamlit

>>> Database : SQLite

>>> AI Layer : Machine Learning / NLP


</div>

""",
unsafe_allow_html=True)




st.divider()





# ================= LANGUAGES =================



st.subheader("🐍 Programming Language")



c1,c2,c3=st.columns(3)



with c1:

    st.markdown("""
<div class="tech-card">


<h2>
🐍 Python
</h2>


<p>

Main programming language used for:

<br><br>

✔ Application Development

<br>

✔ AI Implementation

<br>

✔ Database Connection

</p>


</div>

""",
unsafe_allow_html=True)




with c2:


    st.markdown("""
<div class="tech-card">


<h2>
🌐 HTML/CSS
</h2>


<p>

Used for:

<br><br>

✔ UI Designing

<br>

✔ Attractive Layout

<br>

✔ Custom Styling

</p>


</div>

""",
unsafe_allow_html=True)




with c3:


    st.markdown("""
<div class="tech-card">


<h2>
🗄 SQL
</h2>


<p>

Used for:

<br><br>

✔ Data Storage

<br>

✔ Query Handling

<br>

✔ Report Management

</p>


</div>

""",
unsafe_allow_html=True)






st.divider()





# ================= FRAMEWORK =================



st.subheader("🚀 Framework & Libraries")



cols=st.columns(4)



libraries=[

("⚡ Streamlit",
"Web Application Development"),

("📊 Pandas",
"Data Processing"),

("🤖 Scikit-learn",
"Machine Learning"),

("💾 SQLite3",
"Database Management")

]



for col,data in zip(cols,libraries):


    with col:


        st.success(
        f"""
{data[0]}


{data[1]}
"""
        )





st.divider()





# ================= CONCEPTS =================



st.subheader("🧠 Programming Concepts Applied")



concepts=[

"Functions",

"Conditional Statements",

"Loops",

"File Handling",

"Database Connectivity",

"Modular Programming",

"Data Processing",

"Exception Handling"

]



c1,c2=st.columns(2)



with c1:


    for item in concepts[:4]:

        st.info(
        "✅ "+item
        )



with c2:


    for item in concepts[4:]:

        st.warning(
        "✅ "+item
        )






st.divider()





# ================= PROJECT STRUCTURE =================



st.subheader("📂 Project Architecture")



st.markdown("""
<div class="module">


📁 Campus Safety Incident Logger


<br>

├── app.py

<br>

├── database.py

<br>

├── ai_ml_layer.py

<br>

├── requirements.txt

<br>

└── pages/

<br>

&nbsp;&nbsp;&nbsp;├── Home.py

<br>

&nbsp;&nbsp;&nbsp;├── About.py

<br>

&nbsp;&nbsp;&nbsp;├── Report Incident.py

<br>

&nbsp;&nbsp;&nbsp;├── My Reports.py

<br>

&nbsp;&nbsp;&nbsp;├── Admin Dashboard.py

<br>

&nbsp;&nbsp;&nbsp;├── Analytics.py

<br>

&nbsp;&nbsp;&nbsp;└── Live Demo.py


</div>

""",
unsafe_allow_html=True)






st.divider()





# ================= FOOTER =================



st.markdown("""
<div class="footer">


<h2>
🚀 Built Using Python & Streamlit
</h2>


<p>
Campus Safety Incident Logger | AI & Data Science Project
</p>


</div>

""",
unsafe_allow_html=True)