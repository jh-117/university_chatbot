import streamlit as st
import google.generativeai as genai

# ---------------------
# CONFIG
# ---------------------
# Replace with your Gemini API key from Google AI Studio
API_KEY = "AIzaSyCBO2Fvn-Oky_imBWqeob1VuQ1-VImhP-4"

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------------
# STREAMLIT UI
# ---------------------
st.title("🤖 University Chatbot (Gemini API)")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Ask me anything:")

if st.button("Ask"):
    if user_input:
        # Call Gemini API
        try:
            response = model.generate_content(user_input)
            answer = response.text
        except Exception as e:
            answer = f"⚠️ Error: {str(e)}"

        # Save to history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", answer))

# Show conversation
st.write("### 💬 Conversation")
for speaker, msg in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**👤 {speaker}:** {msg}")
    else:
        st.markdown(f"**🤖 {speaker}:** {msg}")
