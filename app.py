import streamlit as st
from chatbot import ask_bot

st.set_page_config(page_title="Civil War Chatbot", page_icon="🇳🇬", layout="centered")

# DARK GREEN THEME
st.markdown("""
<style>
.chat-bubble-user {
    background-color: #0B6623;
    color: white;
    padding: 12px;
    border-radius: 12px;
    margin: 6px;
    text-align: right;
    font-weight: 500;
}
.chat-bubble-bot {
    background-color: #E8F5E9;
    color: black;
    padding: 12px;
    border-radius: 12px;
    margin: 6px;
    text-align: left;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

st.title("🇳🇬 Nigerian Civil War Chatbot")
st.caption("Ask anything about the war — smart offline AI")

st.markdown("### 💡 Try asking:")
st.write("- Why did the war happen?")
st.write("- Who were the main leaders?")
st.write("- Explain the famine during the war")
st.write("- What role did foreign countries play?")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask your question...")

if user_input:
    response = ask_bot(user_input)

    st.session_state.messages.append(("user", user_input))
    st.session_state.messages.append(("bot", response))

for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"<div class='chat-bubble-user'>👤 {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-bot'>🤖 {msg}</div>", unsafe_allow_html=True)
