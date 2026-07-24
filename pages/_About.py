import streamlit as st

st.title("ℹ️ About Campus Safety Incident Logger")

st.write("""
## 📌 Project Overview

Campus Safety Incident Logger is an AI-based application
designed to help students report safety-related incidents
and improve campus security awareness.

The system provides a digital platform where incidents can
be recorded, analyzed, and monitored for better safety
management.
""")

st.divider()

st.subheader("🎯 Objective")

st.write("""
The main objective of this project is to:
- Create an easy incident reporting system
- Reduce manual reporting difficulties
- Identify safety issues using AI classification
- Provide preventive safety suggestions
""")

st.subheader("✨ Key Features")

features = [
    "Online incident reporting",
    "AI-based incident classification",
    "Preventive suggestions",
    "Admin monitoring dashboard",
    "Incident history tracking",
    "Safety trend analysis"
]

for feature in features:
    st.write("✅", feature)

st.divider()

st.subheader("🛠️ Technologies Used")

st.write("""
- Python
- Streamlit
- SQLite Database
- JSON
- Pandas
- Simple AI/ML Classification
""")

st.divider()

st.subheader("🎓 R23 Academic Alignment")

st.write("""
Integrated Subjects:

• Programming for Problem Solving  
• IT Workshop  
• NSS / Community Service  

The project combines programming skills with social
awareness to address campus safety challenges.
""")

st.success("Campus Safety Incident Logger - Mini Project")