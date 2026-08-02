import streamlit as st
from database import create_table, get_incidents


st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)


create_table()



# ================= CSS =================

st.markdown("""
<style>


.stApp{

background:

linear-gradient(
135deg,
#f1f5f9,
#dbeafe
);

}



/* HERO */


.hero{

background:

linear-gradient(
135deg,
#1e40af,
#0284c7,
#06b6d4
);


padding:55px;


border-radius:35px;


text-align:center;


box-shadow:

0 15px 35px rgba(0,0,0,.2);


color:white;


}



.hero h1{

font-size:55px;

font-weight:900;

}


.hero p{

font-size:22px;

color:#e0f2fe;

}




/* METRIC CARDS */


.metric{


background:white;


padding:25px;


border-radius:25px;


text-align:center;


box-shadow:

0 10px 25px rgba(0,0,0,.12);


border-top:

6px solid #2563eb;


}



.metric h1{

font-size:42px;

color:#1d4ed8;

margin:5px;

}


.metric h3{

color:#475569;

}




/* INCIDENT CARD */


.incident{


background:white;


padding:30px;


border-radius:25px;


box-shadow:

0 8px 25px rgba(0,0,0,.12);


border-left:

8px solid #0284c7;


margin-bottom:20px;


}



.incident h3{

color:#1e40af;

font-size:25px;

}




/* STATUS BADGES */


.pending{

background:#fef3c7;

color:#92400e;

padding:8px 15px;

border-radius:20px;

font-weight:bold;

}



.progress{

background:#dbeafe;

color:#1d4ed8;

padding:8px 15px;

border-radius:20px;

font-weight:bold;

}



.resolved{

background:#dcfce7;

color:#166534;

padding:8px 15px;

border-radius:20px;

font-weight:bold;

}




/* ACTION CARDS */


.action{


background:

linear-gradient(
135deg,
#eff6ff,
#ecfeff
);


padding:25px;


border-radius:22px;


text-align:center;


box-shadow:

0 8px 20px rgba(0,0,0,.12);


border-bottom:

5px solid #0284c7;


}



.action h2{

color:#0369a1;

}




/* FOOTER */


.footer{

text-align:center;

padding:40px;

color:#64748b;

}


</style>

""",
unsafe_allow_html=True)





# ================= HEADER =================



st.markdown("""
<div class="hero">


<h1>
👨‍💼 Admin Control Dashboard
</h1>


<p>
Campus Safety Incident Monitoring & Management Portal
</p>


</div>

""",
unsafe_allow_html=True)



st.write("")





# ================= DATABASE =================


reports=get_incidents()



if reports:

    total=len(reports)

    pending=len(
        [r for r in reports if r[7]=="Pending"]
    )

    progress=len(
        [r for r in reports if r[7]=="In Progress"]
    )

    resolved=len(
        [r for r in reports if r[7]=="Resolved"]
    )


else:

    total=0
    pending=0
    progress=0
    resolved=0






# ================= METRICS =================



st.subheader("📊 Incident Overview")



c1,c2,c3,c4=st.columns(4)



data=[

("📄",total,"Total Reports"),

("🟡",pending,"Pending"),

("🔵",progress,"In Progress"),

("🟢",resolved,"Resolved")

]



for col,item in zip(
[c1,c2,c3,c4],
data
):

    with col:

        st.markdown(f"""

        <div class="metric">


        <h1>{item[0]}</h1>

        <h1>{item[1]}</h1>

        <h3>{item[2]}</h3>


        </div>

        """,
        unsafe_allow_html=True)





st.divider()




# ================= SEARCH =================



st.subheader("🔍 Search Incidents")

search=st.text_input(
"Search by category or location"
)



st.divider()




# ================= INCIDENTS =================



st.subheader("🚨 Incident Reports")



if reports:


    for report in reports:


        incident_id=report[0]

        description=report[1]

        category=report[2]

        location=report[3]

        date=report[4]

        time=report[5]

        status=report[7]

        remarks=report[8] if report[8] else "No remarks available"



        if search and search.lower() not in (
            category.lower()+location.lower()
        ):

            continue




        if status=="Pending":

            badge="""
            <span class="pending">
            🟡 Pending
            </span>
            """


        elif status=="In Progress":

            badge="""
            <span class="progress">
            🔵 In Progress
            </span>
            """


        else:

            badge="""
            <span class="resolved">
            🟢 Resolved
            </span>
            """




        st.markdown(f"""

        <div class="incident">


        <h3>
        🚨 Incident #{incident_id}
        </h3>


        <p>

        📂 <b>Category:</b> {category}

        <br><br>


        📍 <b>Location:</b> {location}


        <br><br>


        📅 <b>Date:</b> {date}


        <br><br>


        🕒 <b>Time:</b> {time}


        <br><br>


        📝 <b>Description:</b>

        <br>

        {description}


        <br><br>


        <b>Status:</b>

        {badge}


        <br><br>


        💬 <b>Remarks:</b>

        {remarks}


        </p>


        </div>

        """,
        unsafe_allow_html=True)



else:


    st.info(
    "No incidents available"
    )




st.divider()




# ================= ACTIONS =================



st.subheader("⚙ Management Actions")



a,b,c=st.columns(3)



actions=[

("✅ Review Reports",
"Check and verify student complaints"),

("📊 Monitor Analytics",
"Analyze incident patterns"),

("🚨 Emergency Handling",
"Take quick safety actions")

]



for col,item in zip(
[a,b,c],
actions
):

    with col:

        st.markdown(f"""

        <div class="action">


        <h2>
        {item[0]}
        </h2>


        <p>
        {item[1]}
        </p>


        </div>


        """,
        unsafe_allow_html=True)





st.divider()




st.markdown("""
<div class="footer">


<h2>
👨‍💼 Admin Dashboard
</h2>


<p>
Campus Safety Incident Logger | Management Portal
</p>


</div>

""",
unsafe_allow_html=True)