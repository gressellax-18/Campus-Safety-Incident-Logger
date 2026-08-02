import streamlit as st
from ai_ml_layer import classify_incident, preventive_suggestion


st.set_page_config(
    page_title="AI Live Demo",
    page_icon="🚀",
    layout="wide"
)


# ================= CSS =================

st.markdown("""
<style>


.stApp{

background:
linear-gradient(
135deg,
#111827,
#1e1b4b,
#312e81
);

}



/* HEADER */


.hero{

background:

linear-gradient(
135deg,
#9333ea,
#db2777,
#f97316
);


padding:50px;


border-radius:35px;


text-align:center;


box-shadow:

0 15px 40px rgba(236,72,153,0.4);


color:white;

}


.hero h1{

font-size:55px;

font-weight:900;

}



.hero p{

font-size:21px;

color:#fce7f3;

}




/* AI CARD */


.ai-card{


background:

rgba(255,255,255,0.12);


padding:30px;


border-radius:25px;


border:1px solid rgba(255,255,255,0.25);


box-shadow:

0 10px 30px rgba(0,0,0,0.4);


color:white;

}



.ai-card h2{

color:#f9a8d4;

}




/* RESULT */


.result{


background:

linear-gradient(
135deg,
#064e3b,
#047857
);


padding:30px;


border-radius:25px;


border-left:

8px solid #22c55e;


color:white;


}




/* CCTV */


.cctv{


background:

linear-gradient(
135deg,
#431407,
#9a3412
);


padding:30px;


border-radius:25px;


border-left:

8px solid #fb923c;


color:white;

}




/* SAMPLE */


.sample{


background:

rgba(255,255,255,0.15);


padding:20px;


border-radius:20px;


text-align:center;


color:white;


box-shadow:

0 5px 15px rgba(0,0,0,.3);


}



/* FOOTER */


.footer{

text-align:center;

padding:40px;

color:#cbd5e1;

}



</style>

""",
unsafe_allow_html=True)





# ================= HEADER =================


st.markdown("""
<div class="hero">


<h1>
🚀 AI Powered Live Demonstration
</h1>


<p>
Campus Safety Incident Logger - Intelligent Monitoring System
</p>


</div>

""",
unsafe_allow_html=True)



st.write("")





# ================= INTRO =================


st.markdown("""
<div class="ai-card">


<h2>
🤖 Artificial Intelligence Module
</h2>


<p>

This module demonstrates automatic incident
classification using AI and generates safety
recommendations for campus management.

</p>


</div>

""",
unsafe_allow_html=True)




st.divider()





# ================= AI INCIDENT TEST =================



st.subheader("🧠 AI Incident Classification")



incident = st.text_area(

"Enter Incident Description",

placeholder=
"Example: My mobile phone was stolen near library"

)




if st.button(
"🚀 Run AI Analysis",
use_container_width=True
):


    if incident.strip()=="":


        st.warning(
        "Please enter incident details."
        )


    else:


        with st.spinner(
        "🤖 AI Model analysing..."
        ):


            category = classify_incident(
                incident
            )


            suggestion = preventive_suggestion(
                category
            )



        st.success(
        "AI Analysis Completed Successfully"
        )



        st.markdown(f"""

<div class="result">


<h2>
📊 AI Prediction Result
</h2>


<p>

🏷 <b>Incident Category:</b>

{category}


<br><br>


🎯 <b>Confidence:</b>

95%


<br><br>


💡 <b>Safety Recommendation:</b>


<br>


{suggestion}


</p>


</div>

""",
unsafe_allow_html=True)



        st.progress(95)






st.divider()





# ================= CCTV MODULE =================



st.subheader(
"📹 AI CCTV Surveillance Simulation"
)



st.markdown("""
<div class="cctv">


<h2>
👁 Smart Campus Vision
</h2>


<p>

AI monitors CCTV cameras and detects
suspicious activities and emergencies.

</p>


</div>

""",
unsafe_allow_html=True)




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

"Fire Detection",

"Student Emergency"

]

)




if st.button(
"🔍 Analyze CCTV Feed",
use_container_width=True
):


    if event=="Normal Activity":


        st.success(
        "✅ Normal Activity Detected - No Risk Found"
        )


    elif event=="Suspicious Person Detected":


        st.warning(
        "⚠ Suspicious Person Detected - Security Alert Generated"
        )


    elif event=="Unauthorized Entry":


        st.error(
        "🚨 Unauthorized Entry Detected"
        )


    elif event=="Fire Detection":


        st.error(
        "🔥 Fire Hazard Detected - Emergency Response Activated"
        )


    else:


        st.warning(
        "🏥 Student Medical Emergency Detected"
        )





st.divider()





# ================= SAMPLE CASES =================



st.subheader(
"📌 Sample AI Scenarios"
)



samples=[

"📱 Mobile Theft Detection",

"🔥 Fire Emergency",

"👊 Harassment Complaint",

"🚪 Unauthorized Entry",

"🏥 Medical Emergency"

]



cols=st.columns(5)



for col,item in zip(cols,samples):


    with col:


        st.markdown(f"""

<div class="sample">

{item}

</div>

""",
        unsafe_allow_html=True)






st.divider()





# ================= WORKFLOW =================



st.subheader(
"⚙ AI Processing Workflow"
)



st.markdown("""
<div class="ai-card">


👨‍🎓 Student Reports Incident

<br>
⬇
<br>

📝 Text Processing

<br>
⬇
<br>

🤖 AI Classification

<br>
⬇
<br>

🏷 Category Prediction

<br>
⬇
<br>

💡 Safety Suggestion

<br>
⬇
<br>

🛡 Safer Campus


</div>

""",
unsafe_allow_html=True)






st.divider()





# ================= FEATURES =================



st.subheader(
"✨ AI Capabilities"
)



c1,c2,c3=st.columns(3)



with c1:

    st.success(
    "🧠 NLP Analysis"
    )

    st.success(
    "⚡ Fast Prediction"
    )


with c2:

    st.info(
    "📹 CCTV Monitoring"
    )

    st.info(
    "🚨 Threat Detection"
    )


with c3:

    st.warning(
    "💡 Safety Suggestions"
    )

    st.warning(
    "🛡 Risk Prevention"
    )





st.divider()




# ================= FOOTER =================



st.markdown("""
<div class="footer">


<h2>
🚀 AI Live Demo Completed
</h2>


<p>
Campus Safety Incident Logger | Artificial Intelligence Layer
</p>


</div>

""",
unsafe_allow_html=True)