import streamlit as st
import pandas as pd

st.title("📊 Analytics Dashboard")

data = pd.DataFrame({
    "Category": ["Theft", "Accident", "Harassment", "Fire"],
    "Count": [12, 8, 5, 3]
})

st.subheader("Category-wise Incidents")
st.bar_chart(data.set_index("Category"))