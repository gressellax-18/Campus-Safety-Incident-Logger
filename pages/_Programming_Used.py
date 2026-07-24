import streamlit as st

st.title("💻 Programming Used")

st.write("""
## Technologies Used

This project is developed using Python programming
and various supporting tools.
""")

st.subheader("🐍 Python")

st.write("""
Python is the main programming language used for:
- Application development
- AI/ML implementation
- Database operations
- Data processing
""")

st.subheader("🛠️ Framework & Libraries")

st.write("""
• Streamlit - Web application framework

• Pandas - Data handling and analysis

• JSON - Data storage and exchange

• SQLite - Database management

• Plotly - Data visualization
""")

st.subheader("📌 Programming Concepts")

for item in [
    "Functions",
    "Conditional Statements",
    "File Handling",
    "Data Structures",
    "Database Connectivity",
    "Modular Programming"
]:
    st.write("✅", item)