import os
import streamlit as st
if "messages" not in st.session_state:
    st.session_state.messages = []
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

st.set_page_config(page_title="Talk To Me",page_icon="🧑‍💻")
@st.cache_resource
def get_client():
    if not os.getenv("GROQ_API_KEY"):
        return None
    return Groq()

client =get_client()

st.title("😁 Chat with The Most Powerfull CHATBOT")

st.sidebar.header("Settings")
model=st.sidebar.selectbox(
    "Model",
    ["llama-3.1-8b-instant","llama-3.3-70b-versatile"],

)
system_prompt=st.sidebar.text_area(
    "System prompt (the bot's personality)",
    "You are a friendly, concise assistant for Indian students learning to code",
)
if st.sidebar.button("Clear chat"):
    st.session_state.messages= []

if client is None:
    st.error("No GROQ_API_KEY found. Create a .env file with GROQ_API_KEY=your_key_here ,"
    "then restart the app." 
    )
    st.stop()

if "message" not in st.session_state:
    st.session_state.message= []

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_text=st.chat_input("Type your message and press ENTER")

if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.write(user_text)

with st.chat_message("assistant"):
        
        messages_to_send = [{"role": "system", "content": system_prompt}]
        messages_to_send.extend(st.session_state.messages)

        stream = client.chat.completions.create(
            model=model,
            messages=messages_to_send,
            temperature=0.4,
            stream=True,
        )
        def token_generator():
            for chunk in stream:
                piece=chunk.choices[0].delta.content
                if piece:
                    yield piece
        reply=st.write_stream(token_generator)

st.session_state.messages.append({"role":"assistant","content":reply})
