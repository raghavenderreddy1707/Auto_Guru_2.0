import streamlit as st
import wikipedia

# App Title and Intro
st.set_page_config(page_title="AutoGuru", page_icon="🚗")
st.title("🏍️ AutoGuru – Your Ultimate Automotive AI Assistant")
st.write("Ask me anything about cars and bikes – specs, history, comparisons, or maintenance!")

# Sidebar with Suggestions
with st.sidebar:
    st.subheader("💡 Sample Questions")
    st.markdown("- What is ABS in bikes?")
    st.markdown("- Compare Honda Activa and TVS Jupiter")
    st.markdown("- Tell me about electric cars")
    st.markdown("- What engine does Royal Enfield use?")
    st.markdown("- What is a hybrid car?")

# Input Area
user_question = st.text_input("🔍 Enter your automotive question:")

# Display Search Result
if user_question:
    with st.spinner("🔧 AutoGuru is fetching your answer..."):
        try:
            summary = wikipedia.summary(user_question, sentences=3)
            with st.expander("✅ Answer from AutoGuru"):
                st.write(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            st.warning("🛑 Your question is too broad. Try one of these topics:")
            for option in e.options[:5]:
                st.write("•", option)
        except wikipedia.exceptions.PageError:
            st.error("❌ Sorry, I couldn't find anything. Try rephrasing your question.")
        except Exception as e:
            st.error("⚠️ Something went wrong. Please try again later.")

# History
if "history" not in st.session_state:
    st.session_state.history = []

if user_question and user_question not in st.session_state.history:
    st.session_state.history.append(user_question)

# Display History
if st.session_state.history:
    st.subheader("🕘 Your Questions")
    for q in st.session_state.history[::-1]:
        st.markdown(f"• {q}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Wikipedia | @AutoGuru")
