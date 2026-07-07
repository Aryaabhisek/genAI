import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

# -------------------------
# Load Environment Variables
# -------------------------
load_dotenv()

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Funny AI Chatbot",
    page_icon="🤖",
    layout="centered",
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#141E30,#243B55);
}

.main-title{
    text-align:center;
    color:white;
    font-size:40px;
    font-weight:bold;
    margin-bottom:5px;
}

.sub-title{
    text-align:center;
    color:#dddddd;
    margin-bottom:30px;
}

.chat-container{
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Title
# -------------------------
st.markdown("<div class='main-title'>🤖 Funny AI Chatbot</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>Powered by Mistral AI</div>",
    unsafe_allow_html=True,
)

# -------------------------
# Load Model
# -------------------------
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

# -------------------------
# Session State
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a Funny AI Agent")
    ]

if "display_messages" not in st.session_state:
    st.session_state.display_messages = []

# -------------------------
# Display Previous Messages
# -------------------------
for msg in st.session_state.display_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# Chat Input
# -------------------------
prompt = st.chat_input("Type your message...")

if prompt:

    # Show User Message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.display_messages.append(
        {"role": "user", "content": prompt}
    )

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # AI Response
    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    st.session_state.display_messages.append(
        {"role": "assistant", "content": response.content}
    )

    with st.chat_message("assistant"):
        st.markdown(response.content)