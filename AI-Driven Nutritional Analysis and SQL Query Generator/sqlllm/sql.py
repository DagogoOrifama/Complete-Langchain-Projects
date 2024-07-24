from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Google API key for generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    """Fetch response from Gemini model based on question and prompt."""
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    sql_query = response.text.strip()
    result = execute_sql_query(sql_query, "test.db")
    return result

def execute_sql_query(query, db_path):
    """Execute the SQL query and fetch results."""
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
    return rows

# Prompt definition
prompt = [
    """
    You are an expert in converting English questions to SQL code!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION
    
    For example,
    Example 1 - How many entries of records are present?, 
    the SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
    Also, the SQL code should not have ``` in the beginning or end and sql word in output.
    """
]

# Initialize Streamlit app
st.set_page_config(page_title="SQL Query Retriever")
st.header("Gemini Application")

questions = st.text_input("Input:", key="input")
if st.button("Ask the question"):
    response = get_gemini_response(questions, prompt)
    st.subheader("The Response is")
    for row in response:
        st.write(row)
