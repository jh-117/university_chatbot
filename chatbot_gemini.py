import streamlit as st
import google.generativeai as genai

# Configure API key securely from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🎓 University Chatbot (Gemini API)")

# Input box
user_input = st.text_input("Ask me anything about university life:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question!")
    else:
        try:
            response = model.generate_content(user_input)
            st.success(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

