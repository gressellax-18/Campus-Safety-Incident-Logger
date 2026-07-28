import streamlit as st
import pandas as pd
from database import create_table, get_incidents

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

create_table()

st.title("📊 Analytics Dashboard")
st.write("Live analysis of all reported campus incidents.")

st.divider()

reports = get_incidents()

if reports:

    # Convert database records to DataFrame
    df = pd.DataFrame(reports, columns=[
        "ID",
        "Description",
        "Category",
        "Location",
        "Incident Date",
        "Incident Time",
        "Reported Time",
        "Status",
        "Remarks"
    ])

    # ---------------- Metrics ----------------
    total = len(df)
    pending = len(df[df["Status"] == "Pending"])
    progress = len(df[df["Status"] == "In Progress"])
    resolved = len(df[df["Status"] == "Resolved"])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📄 Total Reports", total)
    c2.metric("🟡 Pending", pending)
    c3.metric("🔵 In Progress", progress)
    c4.metric("🟢 Resolved", resolved)

    st.divider()

    # ---------------- Category Chart ----------------
    st.subheader("📂 Incident Category Distribution")

    category_counts = df["Category"].value_counts()

    st.bar_chart(category_counts)

    st.divider()

    # ---------------- Status Chart ----------------
    st.subheader("📌 Incident Status Distribution")

    status_counts = df["Status"].value_counts()

    st.bar_chart(status_counts)

    st.divider()

    # ---------------- Recent Reports ----------------
    st.subheader("📋 Recent Reports")

    st.dataframe(
        df[[
            "ID",
            "Category",
            "Location",
            "Status",
            "Incident Date"
        ]],
        use_container_width=True
    )

else:

    st.info("No incident reports available.")

st.divider()

st.success("📈 Analytics are generated automatically from the incident database.")

st.caption("Campus Safety Incident Logger | Analytics Dashboard")