import streamlit as st
from ai_ml_layer import classify_incident, preventive_suggestion

st.title("🤖 AI / ML Layer")

st.write("""
### Artificial Intelligence in Campus Safety

The AI/ML layer analyzes reported incidents,
classifies them into categories, and provides
preventive safety suggestions.
""")

st.divider()

st.subheader("🔄 AI Working Process")

st.code("""
Student Incident Report
          ↓
Text Analysis
          ↓
Incident Classification
          ↓
Category Prediction
          ↓
Preventive Suggestion
""")

st.subheader("🧠 AI Features")

features = [
    "Automatic incident classification",
    "Safety issue identification",
    "Preventive measure suggestion",
    "Support for campus safety improvement"
]

for feature in features:
    st.write("✅", feature)


st.divider()

st.subheader("🧪 AI Live Testing")

incident = st.text_area(
    "Enter an incident description:",
    placeholder="Example: Street light is not working near hostel"
)

if st.button("Analyze Incident"):

    if incident.strip() == "":
        st.warning("Please enter incident details")

    else:
        category = classify_incident(incident)
        suggestion = preventive_suggestion(category)

        st.success("Analysis Completed")

        st.write("### 📌 AI Result")

        st.write("**Incident Category:**", category)

        st.write("**Preventive Suggestion:**", suggestion)


st.divider()

st.subheader("📌 AI Contribution")

st.write("""
AI helps the system by:
- Reducing manual classification work
- Identifying common campus safety problems
- Providing quick preventive solutions
- Supporting better decision making
""")