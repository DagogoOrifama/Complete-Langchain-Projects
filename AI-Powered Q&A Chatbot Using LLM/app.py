# Q&A Chatbot
from langchain.llms import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_openai_response(query):
    """Fetch response from OpenAI model."""
    model = OpenAI(model_name="text-davinci-003", temperature=0.5)
    return model(query)

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

def main():
    """Main function to run the app."""
    user_input = st.text_input("Input:", key="user_input")
    
    if st.button("Ask the question"):
        if user_input:
            response = fetch_openai_response(user_input)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
