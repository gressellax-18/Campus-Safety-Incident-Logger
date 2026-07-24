import streamlit as st

st.title("📚 Subjects Used")

st.write("""
The Campus Safety Incident Logger project integrates
concepts from different R23 curriculum subjects.
""")

st.divider()

st.subheader("🎓 Subject Integration")

subjects = {
    "Subject": [
        "Programming for Problem Solving",
        "IT Workshop",
        "NSS / Community Service"
    ],
    "Contribution": [
        "Python programming, logic building, file handling and problem solving",
        "Software tools, application development and technical implementation",
        "Social awareness, campus safety improvement and community responsibility"
    ]
}

st.table(subjects)

st.divider()

st.subheader("📌 Topics Applied")

topics = [
    "File Handling",
    "Internet Tools",
    "Database Management",
    "Social Awareness",
    "Data Processing",
    "Problem Solving"
]

for topic in topics:
    st.write("✅", topic)

st.divider()

st.subheader("🔗 R23 Alignment")

st.write("""
**Semester-I: Programming Concepts**

- Python programming
- File handling
- Data processing

**Semester-II: NSS / Community Service**

- Social responsibility
- Safety awareness
- Community problem identification
""")

st.success("Subjects successfully integrated into the mini project.")