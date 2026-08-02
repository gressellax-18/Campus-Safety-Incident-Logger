import streamlit as st
from database import create_table, get_incidents


st.set_page_config(
    page_title="My Reports",
    page_icon="📄",
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
#eef2ff,
#f8fafc,
#e0f2fe
);

}



/* HEADER */


.header{


background:

linear-gradient(
135deg,
#2563eb,
#06b6d4
);


padding:45px;


border-radius:30px;


text-align:center;


color:white;


box-shadow:

0 15px 35px rgba(37,99,235,.3);


}


.header h1{

font-size:48px;

font-weight:900;

}



.header p{

font-size:20px;

color:#e0f2fe;

}




/* REPORT CARD */


.report-card{


background:white;


padding:25px;


border-radius:25px;


margin-bottom:20px;


box-shadow:

0 8px 25px rgba(0,0,0,.12);


border-left:

8px solid #2563eb;


}




.report-card h2{

color:#1e3a8a;

}




/* INFO BOX */


.info-box{


background:#eff6ff;


padding:18px;


border-radius:15px;


border-left:

6px solid #3b82f6;


}




/* STATUS */


.pending{


background:#fef3c7;


color:#92400e;


padding:8px 15px;


border-radius:20px;


font-weight:bold;


}


.viewed{


background:#dbeafe;


color:#1d4ed8;


padding:8px 15px;


border-radius:20px;


font-weight:bold;


}



.progress{


background:#ede9fe;


color:#6d28d9;


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




.footer{


text-align:center;


padding:35px;


color:#64748b;


}



</style>

""",
unsafe_allow_html=True)





# ================= HEADER =================



st.markdown("""
<div class="header">


<h1>
📄 My Incident Reports
</h1>


<p>
Track your complaints and monitor resolution status
</p>


</div>

""",
unsafe_allow_html=True)



st.write("")





# ================= SEARCH =================



search = st.text_input(

"🔍 Search Your Reports",

placeholder="Search by category or description..."

)



st.divider()





# ================= DATA =================



reports = get_incidents()



if reports:


    total=len(reports)


    st.metric(
        "📋 Total Submitted Reports",
        total
    )


    st.divider()



    for report in reports:



        incident_id = report[0]

        description = report[1]

        category = report[2]

        location = report[3]

        date = report[4]

        time = report[5]

        reported_time = report[6]

        status = report[7]

        remarks = report[8] if report[8] else "No remarks from management"





        # SEARCH FILTER


        if search:


            if (

            search.lower() not in description.lower()

            and

            search.lower() not in category.lower()

            ):

                continue





        # STATUS DESIGN


        if status=="Pending":


            badge="""

<span class="pending">

🟡 Pending

</span>

"""


            progress_value=25



        elif status=="Viewed":


            badge="""

<span class="viewed">

👀 Viewed

</span>

"""


            progress_value=50



        elif status=="In Progress":


            badge="""

<span class="progress">

🔵 In Progress

</span>

"""


            progress_value=75



        else:


            badge="""

<span class="resolved">

🟢 Resolved

</span>

"""


            progress_value=100






        # REPORT CARD



        st.markdown(f"""

<div class="report-card">


<h2>

🚨 Incident #{incident_id}

</h2>



<div class="info-box">


<b>📂 Category:</b>

{category}


<br><br>


<b>📍 Location:</b>

{location}


<br><br>


<b>📅 Incident Date:</b>

{date}


<br><br>


<b>🕒 Incident Time:</b>

{time}


<br><br>


<b>⏰ Reported On:</b>

{reported_time}


</div>



<br>



<b>📝 Description</b>


<p>

{description}

</p>



<br>


<b>Status:</b>

{badge}



<br><br>


<b>Progress Tracking</b>


</div>


""",
unsafe_allow_html=True)



        st.progress(
            progress_value/100
        )



        st.info(
        f"💬 Management Remarks: {remarks}"
        )


        st.divider()




else:


    st.warning(
    "No incident reports available."
    )






# ================= FOOTER =================



st.markdown("""
<div class="footer">


<h3>
🛡 Campus Safety Incident Logger
</h3>


<p>
Student Complaint Tracking Portal
</p>


</div>

""",
unsafe_allow_html=True)