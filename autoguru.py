import streamlit as st
import wikipedia
import openai
import os

# Set your OpenAI API Key here
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "your-api-key-here"

st.set_page_config(page_title="AutoGuru", page_icon="🚗")
st.title("🏍️ AutoGuru – Ask Me Anything!")

st.write("I'm your AI assistant for cars, bikes, and anything else you'd like to know.")

# Sidebar with example questions
with st.sidebar:
    st.subheader("💡 Try asking:")
    st.markdown("- What is a turbocharger?")
    st.markdown("- How does ABS work?")
    st.markdown("- Who invented the motorcycle?")
    st.markdown("- How to boost mileage of a bike?")
    st.markdown("- What is Python used for?")

# Question input
user_input = st.text_input("🔍 Ask your question:")

# Ask GPT (OpenAI)
def ask_gpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are AutoGuru, an expert AI assistant in automobiles and general knowledge."},
                {"role": "user", "content": question}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Try Wikipedia first
def ask_wikipedia(question):
    try:
        return wikipedia.summary(question, sentences=3)
    except:
        return None

# Answer Logic
if user_input:
    with st.spinner("Thinking..."):
        answer = ask_wikipedia(user_input)
        if not answer:
            answer = ask_gpt(user_input)
        st.success("✅ Answer:")
        st.write(answer)
