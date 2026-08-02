import streamlit as st


st.set_page_config(
    page_title="About Campus Safety",
    page_icon="📖",
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
#111827,
#312e81
);

color:white;

}



/* Hero */


.hero{

background:

linear-gradient(
135deg,
#7c3aed,
#2563eb
);


padding:70px;


border-radius:35px;


text-align:center;


box-shadow:

0 20px 50px rgba(0,0,0,.5);


}


.hero h1{

font-size:60px;

font-weight:900;

}



.hero p{

font-size:22px;

color:#ddd6fe;

}



/* Glass */


.glass{


background:

rgba(255,255,255,0.12);


backdrop-filter:blur(15px);


padding:35px;


border-radius:25px;


border:

1px solid rgba(255,255,255,.2);


box-shadow:

0 15px 40px rgba(0,0,0,.3);


}




.glass h2{

color:#c4b5fd;

}



/* Problem */


.problem{


background:

linear-gradient(
135deg,
#7f1d1d,
#991b1b
);


padding:30px;


border-radius:25px;


}



/* Solution */


.solution{


background:

linear-gradient(
135deg,
#065f46,
#059669
);


padding:30px;


border-radius:25px;


}



/* Cards */


.card{


background:

rgba(255,255,255,.1);


padding:25px;


border-radius:20px;


text-align:center;


height:180px;


border:

1px solid rgba(255,255,255,.2);


}



.card h2{

color:#93c5fd;

}




/* Architecture */


.flow{


background:

rgba(255,255,255,.08);


padding:30px;


border-radius:25px;


text-align:center;


font-size:20px;


line-height:2.2;


}





.footer{

text-align:center;

padding:40px;

color:#cbd5e1;


}


</style>

""",
unsafe_allow_html=True)




# ================= HERO =================



st.markdown("""
<div class="hero">


<h1>
📖 About Project
</h1>


<p>
Campus Safety Incident Logger
</p>


<p>
AI Powered Digital Safety Ecosystem
</p>


</div>

""",
unsafe_allow_html=True)



st.write("")




# ================= INTRO =================



st.markdown("""
<div class="glass">


<h2>
🚀 Project Vision
</h2>


<p>

Campus Safety Incident Logger aims to create a
safer educational environment by providing a
digital platform for reporting, monitoring and
resolving campus incidents.

The system combines web technology,
database management and artificial intelligence
to improve safety response.

</p>


</div>

""",
unsafe_allow_html=True)




st.write("")




# ================= PROBLEM SOLUTION =================


col1,col2=st.columns(2)



with col1:


    st.markdown("""
    <div class="problem">


    <h2>
    🚨 Existing Challenges
    </h2>


    <p>

    ❌ Manual complaint process

    <br><br>

    ❌ Delayed communication

    <br><br>

    ❌ No tracking mechanism

    <br><br>

    ❌ Poor data management


    </p>


    </div>

    """,
    unsafe_allow_html=True)





with col2:


    st.markdown("""
    <div class="solution">


    <h2>
    💡 Our Solution
    </h2>


    <p>

    ✅ Digital reporting

    <br><br>

    ✅ AI based analysis

    <br><br>

    ✅ Admin dashboard

    <br><br>

    ✅ Smart tracking


    </p>


    </div>

    """,
    unsafe_allow_html=True)




st.divider()




# ================= MISSION =================



st.subheader("🎯 Project Mission")



a,b,c=st.columns(3)



for col,data in zip(
[a,b,c],
[
("🛡 Protection",
"Improve student safety"),

("⚡ Response",
"Reduce reaction time"),

("🤖 Intelligence",
"Use AI for smart decisions")
]
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




# ================= ARCHITECTURE =================



st.subheader("⚙ System Architecture")



st.markdown("""
<div class="flow">


👨‍🎓 Student


⬇


🚨 Incident Reporting Module


⬇


🤖 AI Classification Engine


⬇


💾 SQLite Database


⬇


👨‍💼 Admin Dashboard


⬇


📊 Analytics & Resolution


</div>

""",
unsafe_allow_html=True)




st.divider()




# ================= IMPACT =================



st.subheader("📈 Project Impact")



x,y,z,w=st.columns(4)



for col,data in zip(
[x,y,z,w],
[
("🚨","Quick Reporting"),
("🤖","AI Support"),
("📊","Data Analysis"),
("🛡","Safe Campus")
]
):

    with col:

        st.markdown(f"""

        <div class="card">


        <h1>{data[0]}</h1>


        <h3>{data[1]}</h3>


        </div>


        """,
        unsafe_allow_html=True)




st.divider()




# ================= FOOTER =================



st.markdown("""
<div class="footer">


<h2>
📖 Campus Safety Incident Logger
</h2>


<p>
Making Campuses Safer with Artificial Intelligence
</p>


</div>

""",
unsafe_allow_html=True)