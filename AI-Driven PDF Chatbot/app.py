import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_text_from_pdfs(pdf_files):
    """Extract text from a list of PDF files."""
    combined_text = ""
    for pdf in pdf_files:
        reader = PdfReader(pdf)
        for page in reader.pages:
            combined_text += page.extract_text()
    return combined_text

def split_text_into_chunks(text):
    """Split text into smaller chunks."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = splitter.split_text(text)
    return chunks

def create_vector_store_from_chunks(chunks):
    """Create a vector store from text chunks."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def initialize_conversational_chain():
    """Initialize the conversational chain with a prompt template."""
    template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in
    the provided context, just say, "answer is not available in the context", don't provide the wrong answer.
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def handle_user_input(question):
    """Handle the user's question and return a response."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("faiss_index", embeddings)
    documents = vector_store.similarity_search(question)
    chain = initialize_conversational_chain()
    response = chain({"input_documents": documents, "question": question}, return_only_outputs=True)
    st.write("Reply:", response["output_text"])

def main():
    st.set_page_config(page_title="Chat with PDF using Gemini")
    st.header("Chat with PDF using Gemini💁")

    question = st.text_input("Ask a Question from the PDF Files")
    if question:
        handle_user_input(question)

    with st.sidebar:
        st.title("Menu:")
        pdf_files = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = extract_text_from_pdfs(pdf_files)
                text_chunks = split_text_into_chunks(raw_text)
                create_vector_store_from_chunks(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()
