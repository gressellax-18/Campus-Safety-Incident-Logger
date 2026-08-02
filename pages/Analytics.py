import streamlit as st
import pandas as pd
from database import create_table, get_incidents


st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
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
#f8fafc,
#e0f2fe
);

}



/* HEADER */

.hero{


background:

linear-gradient(
135deg,
#0f172a,
#1e3a8a,
#0369a1
);


padding:50px;


border-radius:30px;


text-align:center;


box-shadow:

0 15px 35px rgba(0,0,0,0.18);


color:white;

}


.hero h1{

font-size:52px;

font-weight:900;

}



.hero p{

font-size:20px;

color:#bae6fd;

}



/* METRIC CARDS */


.metric{


background:white;


padding:25px;


border-radius:25px;


text-align:center;


box-shadow:

0 8px 20px rgba(0,0,0,.12);


border-bottom:

6px solid #f97316;


}



.metric h1{

font-size:45px;

color:#1e40af;

margin:5px;

}



.metric h3{

color:#475569;

}




/* CHART CARD */


.chart-card{


background:white;


padding:25px;


border-radius:25px;


box-shadow:

0 8px 20px rgba(0,0,0,.12);


border-left:

6px solid #0284c7;


margin-bottom:20px;


}



/* TABLE CARD */


.table-card{


background:white;


padding:20px;


border-radius:20px;


box-shadow:

0 8px 20px rgba(0,0,0,.12);


border-top:

5px solid #1e40af;


}




/* INSIGHT */


.insight{


background:

linear-gradient(
135deg,
#eff6ff,
#ffffff
);


padding:20px;


border-radius:20px;


text-align:center;


box-shadow:

0 8px 18px rgba(0,0,0,.1);


border-left:

5px solid #0891b2;


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
<div class="hero">


<h1>
📊 Analytics Dashboard
</h1>


<p>
Smart Incident Data Analysis & Campus Safety Insights
</p>


</div>

""",
unsafe_allow_html=True)



st.write("")





# ================= DATABASE =================



reports = get_incidents()




if reports:


    df = pd.DataFrame(
        reports,
        columns=[
            "ID",
            "Description",
            "Category",
            "Location",
            "Incident Date",
            "Incident Time",
            "Reported Time",
            "Status",
            "Remarks"
        ]
    )


    total = len(df)


    pending = len(
        df[df["Status"]=="Pending"]
    )


    progress = len(
        df[df["Status"]=="In Progress"]
    )


    resolved = len(
        df[df["Status"]=="Resolved"]
    )


else:


    df=pd.DataFrame()

    total=0
    pending=0
    progress=0
    resolved=0





# ================= METRICS =================



st.subheader("📌 Safety Overview")



c1,c2,c3,c4 = st.columns(4)



metrics=[

("📄",total,"Total Reports"),

("🟡",pending,"Pending"),

("🔵",progress,"In Progress"),

("🟢",resolved,"Resolved")

]



for col,item in zip(
[c1,c2,c3,c4],
metrics
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





# ================= ANALYTICS =================



if not df.empty:


    st.subheader("📈 Incident Analytics")



    col1,col2 = st.columns(2)



    with col1:


        st.markdown(
        """
        <div class="chart-card">
        """,
        unsafe_allow_html=True
        )


        st.subheader(
        "📂 Category Distribution"
        )


        category_data = (
            df["Category"]
            .value_counts()
        )


        st.bar_chart(
            category_data
        )


        st.markdown(
        "</div>",
        unsafe_allow_html=True
        )




    with col2:


        st.markdown(
        """
        <div class="chart-card">
        """,
        unsafe_allow_html=True
        )


        st.subheader(
        "📌 Status Distribution"
        )


        status_data = (
            df["Status"]
            .value_counts()
        )


        st.bar_chart(
            status_data
        )


        st.markdown(
        "</div>",
        unsafe_allow_html=True
        )






    st.divider()




    # ================= LOCATION =================


    st.subheader(
    "📍 Location Wise Analysis"
    )


    location_data = (
        df["Location"]
        .value_counts()
    )


    st.bar_chart(
        location_data
    )





    st.divider()




    # ================= TABLE =================


    st.subheader(
    "📋 Recent Incident Records"
    )



    st.markdown(
    """
    <div class="table-card">
    """,
    unsafe_allow_html=True
    )



    st.dataframe(

        df[
        [
        "ID",
        "Category",
        "Location",
        "Status",
        "Incident Date"
        ]
        ],

        use_container_width=True

    )



    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )



else:


    st.info(
    "📭 No incident reports available."
    )





st.divider()





# ================= INSIGHTS =================



st.subheader(
"💡 Safety Intelligence"
)



a,b,c = st.columns(3)



with a:

    st.markdown("""
    <div class="insight">

    📊

    <h3>
    Data Analysis
    </h3>

    Identify incident patterns

    </div>
    """,
    unsafe_allow_html=True)




with b:


    st.markdown("""
    <div class="insight">

    🔍

    <h3>
    Risk Detection
    </h3>

    Find safety problems

    </div>
    """,
    unsafe_allow_html=True)




with c:


    st.markdown("""
    <div class="insight">

    🚨

    <h3>
    Quick Response
    </h3>

    Improve campus safety

    </div>
    """,
    unsafe_allow_html=True)





st.divider()





# ================= FOOTER =================



st.markdown("""
<div class="footer">


<h2>
📊 Campus Safety Analytics
</h2>


<p>
Campus Safety Incident Logger | Data Driven Safety Management
</p>


</div>

""",
unsafe_allow_html=True)