import streamlit as st

st.set_page_config(
    page_title="Campus Safety Incident Logger",
    page_icon="🛡️",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
    background:#F4F7FC;
}

.main-title{
    text-align:center;
    color:#1E3A8A;
    font-size:42px;
    font-weight:bold;
}

.metric{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,.08);
    text-align:center;
}

.metric h2{
    margin:0;
    color:#2563EB;
}

.metric h1{
    margin:0;
    color:black;
}

.status-pending{
background:#FEF3C7;
padding:6px 12px;
border-radius:20px;
color:#92400E;
font-weight:bold;
}

.status-progress{
background:#DBEAFE;
padding:6px 12px;
border-radius:20px;
color:#1D4ED8;
font-weight:bold;
}

.status-resolved{
background:#DCFCE7;
padding:6px 12px;
border-radius:20px;
color:#15803D;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown(
"<div class='main-title'>🛡️ Campus Safety Incident Logger</div>",
unsafe_allow_html=True)

st.markdown("### 👨‍💼 Admin Dashboard")

# ---------- Metrics ----------
c1,c2,c3,c4=st.columns(4)

with c1:
    st.markdown("""
    <div class="metric">
    <h2>Total Incidents</h2>
    <h1>11</h1>
    </div>
    """,unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric">
    <h2>Pending</h2>
    <h1 style='color:#F59E0B;'>11</h1>
    </div>
    """,unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric">
    <h2>In Progress</h2>
    <h1 style='color:#2563EB;'>0</h1>
    </div>
    """,unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric">
    <h2>Resolved</h2>
    <h1 style='color:#16A34A;'>0</h1>
    </div>
    """,unsafe_allow_html=True)

st.divider()

# ---------- Search ----------
st.text_input("🔍 Search Incident")

# ---------- Incident Cards ----------

for i in range(11,0,-1):

    with st.expander(f"🚨 Incident #{i}"):

        col1,col2=st.columns(2)

        with col1:
            st.write("*Category:* Ragging")
            st.write("*Location:* Block A")
            st.write("*Reported By:* Student")

        with col2:
            st.markdown(
            "<span class='status-pending'>Pending</span>",
            unsafe_allow_html=True)

        st.write("*Description:* Student reported a safety issue inside the campus.")

        c1,c2,c3=st.columns(3)

        with c1:
            st.button("🟡 Mark Progress",key=f"p{i}")

        with c2:
            st.button("🟢 Resolve",key=f"r{i}")

        with c3:
            st.button("🗑️ Delete",key=f"d{i}")