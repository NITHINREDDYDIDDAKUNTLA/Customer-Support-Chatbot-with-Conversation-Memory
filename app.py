import streamlit as st
from langchain_groq import ChatGroq
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv
import os

load_dotenv()

# Customer Support System Prompt
SYSTEM_PROMPT = """You are a helpful Customer Support Assistant for an online store.
- Be polite and friendly
- Answer customer queries about orders, returns, products
- If you don't know, say 'Let me connect you to human agent'
- Keep answers short and helpful
"""

st.title("🛍️ Customer Support Bot")

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(k=2)

if "messages" not in st.session_state:
    st.session_state.messages = []

llm = ChatGroq(
    model="openai/gpt-oss-120b", 
    temperature=0.3
)

conversation = ConversationChain(
    llm=llm, 
    memory=st.session_state.memory,
    verbose=False
)

# Show old chats
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("How can I help you today?")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Add system prompt to query
    full_prompt = f"{SYSTEM_PROMPT}\n\nCustomer: {prompt}"
    result = conversation.invoke({"input": full_prompt})
    
    with st.chat_message("assistant"):
        st.write(result["response"])
    
    st.session_state.messages.append({"role":"assistant","content":result["response"]})
