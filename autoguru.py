# app.py
import streamlit as st

st.title("🚗 AutoGuru AI Assistant")
st.subheader("Ask me anything about cars and bikes!")

query = st.text_input("Enter your question")

if query:
    st.write("🔧 Working on your query:", query)
    # Placeholder for real answer fetching logic
    st.success("✅ Example: ABS stands for Anti-lock Braking System.")
