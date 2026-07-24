import streamlit as st
from ai_ml_layer import classify_incident, preventive_suggestion

st.title("🚀 Campus Safety Incident Logger - Live Demo")

st.write("""
This live demo shows how the system analyzes a reported
campus incident using the AI/ML layer and provides
preventive suggestions.
""")

st.divider()

st.subheader("📝 Enter Incident Details")

incident = st.text_area(
    "Describe the incident:",
    placeholder="Example: Street light is not working near hostel area"
)

if st.button("🔍 Analyze Incident"):

    if incident.strip() == "":
        st.warning("Please enter an incident description")

    else:
        category = classify_incident(incident)
        suggestion = preventive_suggestion(category)

        st.success("Incident Analysis Completed")

        st.subheader("📊 AI Analysis Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Predicted Category",
                category
            )

        with col2:
            st.metric(
                "Status",
                "Analyzed"
            )

        st.subheader("💡 Preventive Suggestion")

        st.info(suggestion)


st.divider()

st.subheader("🔄 Demo Workflow")

st.code("""
Student Reports Incident
          ↓
AI/ML Classification
          ↓
Category Prediction
          ↓
Preventive Suggestion
          ↓
Safety Improvement
""")