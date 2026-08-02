import streamlit as st

from datetime import datetime

from database import add_incident



# ================= CSS =================


st.markdown("""
<style>


/* Background */


.stApp{

background:
linear-gradient(
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
#991b1b,
#dc2626,
#ef4444
);

padding:45px;

border-radius:30px;

text-align:center;

color:white;

box-shadow:
0 20px 40px rgba(0,0,0,.25);

}



.hero h1{

font-size:48px;

font-weight:900;

}



.hero p{

font-size:20px;

color:#fee2e2;

}




/* Section */


.section{

font-size:32px;

font-weight:900;

color:#111827;

margin-top:25px;

}




/* Card */


.card{

background:white;

padding:25px;

border-radius:22px;

box-shadow:
0 10px 25px rgba(0,0,0,.12);

}




/* Preview */


.preview{

background:
linear-gradient(
135deg,
#eff6ff,
#dbeafe
);

padding:25px;

border-radius:20px;

border-left:8px solid #2563eb;

}




/* Warning */


.warning{

background:#fff7ed;

padding:25px;

border-radius:20px;

border-left:8px solid #f97316;

}




/* Success */


.success-box{

background:#ecfdf5;

padding:25px;

border-radius:20px;

border-left:8px solid #16a34a;

}




/* Footer */


.footer{

text-align:center;

padding:30px;

color:gray;

}


</style>


""",
unsafe_allow_html=True)





# ================= HEADER =================



st.markdown("""
<div class="hero">

<h1>🚨 Report Campus Incident</h1>

<p>
Submit Safety Issues Quickly and Securely
</p>

<p>
Report • Track • Resolve
</p>

</div>

""",
unsafe_allow_html=True)




st.write("")





# ================= INTRO =================



st.markdown(
'<div class="section">🛡 Incident Reporting Portal</div>',
unsafe_allow_html=True
)



st.markdown("""
<div class="card">


<h2>
📌 How it Works?
</h2>


<p>

Students can submit campus safety incidents through this
digital reporting system.

The complaint will be stored securely and forwarded to
management for further action.

</p>


</div>

""",
unsafe_allow_html=True)



st.divider()





# ================= FORM =================



st.markdown(
'<div class="section">📝 Incident Details</div>',
unsafe_allow_html=True
)




left,right = st.columns(2)





with left:


    description = st.text_area(

        "📝 Describe Incident",

        placeholder=
        "Explain what happened in detail...",

        height=150

    )



    category = st.selectbox(

        "📂 Incident Category",

        [

        "Ragging",

        "Harassment",

        "Theft",

        "Medical Emergency",

        "Fire Accident",

        "Suspicious Activity",

        "Other"

        ]

    )



    location = st.text_input(

        "📍 Incident Location",

        placeholder=
        "Example: Library, Hostel Block A"

    )







with right:


    incident_date = st.date_input(

        "📅 Incident Date"

    )



    incident_time = st.time_input(

        "🕒 Incident Time"

    )



    severity = st.selectbox(

        "🚦 Severity Level",

        [

        "Low",

        "Medium",

        "High",

        "Critical"

        ]

    )



    st.info(
    f"""
    ⏰ Report Generated Time

    {datetime.now().strftime('%d-%m-%Y %I:%M %p')}
    """
    )





st.divider()





# ================= PREVIEW =================



st.markdown(
'<div class="section">👀 Report Preview</div>',
unsafe_allow_html=True
)




st.markdown(f"""

<div class="preview">


<h3>
🚨 Incident Summary
</h3>


<b>📂 Category:</b> {category}

<br><br>


<b>📍 Location:</b> {location}

<br><br>


<b>🚦 Severity:</b> {severity}

<br><br>


<b>📅 Date:</b> {incident_date}

<br><br>


<b>🕒 Time:</b> {incident_time}


</div>


""",
unsafe_allow_html=True)




st.write("")





# ================= SUBMIT =================



if st.button(

"🚨 Submit Incident Report",

use_container_width=True

):


    if description.strip()=="" or location.strip()=="":


        st.error(
        "❌ Please fill all required fields."
        )


    else:


        reported_time=datetime.now()



        add_incident(

            description,

            category,

            location,

            str(incident_date),

            str(incident_time),

            reported_time.strftime(
            "%Y-%m-%d %H:%M:%S"
            )

        )



        st.markdown("""
        <div class="success-box">

        <h2>
        ✅ Report Submitted Successfully
        </h2>


        <p>

        Your complaint has been recorded.

        Current Status:

        <br><br>

        🟡 Pending Review

        </p>


        </div>

        """,
        unsafe_allow_html=True)



        st.balloons()






st.divider()





# ================= GUIDELINES =================



st.markdown(
'<div class="section">📢 Reporting Guidelines</div>',
unsafe_allow_html=True
)



g1,g2=st.columns(2)





with g1:


    st.markdown("""
    <div class="success-box">

    <h3>✅ Do's</h3>


    ✔ Provide accurate details

    <br><br>

    ✔ Mention correct location

    <br><br>

    ✔ Report immediately

    <br><br>

    ✔ Provide genuine information


    </div>
    """,
    unsafe_allow_html=True)






with g2:


    st.markdown("""
    <div class="warning">


    <h3>❌ Don'ts</h3>


    ❌ Submit false complaints

    <br><br>

    ❌ Create duplicate reports

    <br><br>

    ❌ Use inappropriate language

    <br><br>

    ❌ Hide important details


    </div>

    """,
    unsafe_allow_html=True)







st.divider()





# ================= FOOTER =================



st.markdown("""
<div class="footer">


<h3>
🛡 Campus Safety Incident Logger
</h3>


<p>

Student Safety Reporting Portal

<br>

Streamlit • Python • SQLite

</p>


</div>

""",
unsafe_allow_html=True)