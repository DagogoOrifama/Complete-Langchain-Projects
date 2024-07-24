import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure the Streamlit app
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

# Initialize the OpenAI chat model
chat_model = ChatOpenAI(temperature=0.5)

# Initialize the session state for conversation flow
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = [
        SystemMessage(content="You are a comedian AI assistant")
    ]

def get_response_from_chat_model(user_input):
    """Generate a response from the chat model based on user input."""
    st.session_state['conversation_history'].append(HumanMessage(content=user_input))
    response = chat_model(st.session_state['conversation_history'])
    st.session_state['conversation_history'].append(AIMessage(content=response.content))
    return response.content

# User input section
user_input = st.text_input("Input:", key="user_input")

# Button to submit the question
if st.button("Ask the question"):
    response = get_response_from_chat_model(user_input)
    st.subheader("The Response is")
    st.write(response)