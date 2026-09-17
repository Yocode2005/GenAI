from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st



llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

st.title("🤖 AskBuddy - AI QnA Bot")
st.markdown("My QnA Bot with langchain-google-genai and Streamlit !")

if "messages" not in st.session_state:
    st.session_state.messages = [] # session state is used to store the conversation history between the user and the AI assistant. It allows the application to maintain context across multiple interactions, enabling a more coherent and context-aware conversation. By storing messages in session state, the bot can reference previous user inputs and AI responses, enhancing the overall user experience. till refresh of the page.

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).write(content)

query = st.chat_input("Ask me anything...")
if query:
    st.session_state.messages.append({"role": "user", "content": query})# to store the user's message in the session state, preserving the conversation history for context in future interactions.
    st.chat_message("user").write(query)
    res = llm.invoke(query)
    st.chat_message("assistant").write(res.content[0]["text"])
    st.session_state.messages.append({"role": "assistant", "content": res.content[0]["text"]})# to store the AI assistant's response in the session state, maintaining the conversation history for context in future interactions.


# while True:
#     query = input("User: ")
#     if query.lower() in ["exit", "quit","bye"]:
#         print("Goodbye!")
#         break
#     res = llm.invoke(query)
#     print("AI: ",res.content[0]["text"],"\n");