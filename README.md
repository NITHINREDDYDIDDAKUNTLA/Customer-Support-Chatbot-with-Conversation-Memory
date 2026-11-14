# Customer Support Chatbot with Conversation Memory

I built this chatbot because normal bots forget what you said. This one remembers.

It can handle order tracking, returns and product questions like a real support guy.

How I made it:
- Used Streamlit for simple UI
- Groq LLM for fast replies
- Added LangChain memory so it remembers last 2 chats

Try it: ask your order id, then ask how to return it - it will remember.

Setup:
pip install -r requirements.txt
add your GROQ_API_KEY in .env
streamlit run app.py
