import streamlit as st

# Title
st.title("🎓 University Life Q&A Chatbot")

# Predefined keyword-based answers
faq = {
    "library": "📚 The library is located at the Main Campus, Block B, 2nd Floor.",
    "exam": "📝 You can register for exams through the Student Portal under 'Examination Services'.",
    "cafeteria": "🍴 The cafeteria is open from 8:00 AM to 8:00 PM, Monday to Saturday.",
    "password": "🔑 Visit the IT Helpdesk website or email support@university.edu.my to reset your password.",
    "semester": "📆 The new semester starts on 15th September 2025.",
    "canteen": "🥪 The canteen is located next to the sports complex on the ground floor."
}

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Ask me anything about university life:")

if st.button("Ask"):
    if user_input:
        query = user_input.lower().strip()
        response = "🤖 Sorry, I don’t know the answer to that. Please check with the university office."
        
        # Check for keywords
        for keyword, answer in faq.items():
            if keyword in query:
                response = answer
                break
        
        # Save to history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# Display conversation history
st.write("### 💬 Conversation")
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**👤 {speaker}:** {message}")
    else:
        st.markdown(f"**🤖 {speaker}:** {message}")
