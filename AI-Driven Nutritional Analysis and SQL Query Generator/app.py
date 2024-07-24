# Q&A Chatbot
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Google API key for generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(user_input, image_data, prompt_text):
    """Fetch response from Gemini model based on input, image, and prompt."""
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([user_input, image_data[0], prompt_text])
    return response.text

def input_image_setup(uploaded_file):
    """Prepare image data for the generative model."""
    if uploaded_file:
        image_bytes = uploaded_file.getvalue()
        return [{"mime_type": uploaded_file.type, "data": image_bytes}]
    raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

user_input = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image.", use_column_width=True)

if st.button("Tell me about the image"):
    image_data = input_image_setup(uploaded_file)
    input_prompt = """
    You are an expert nutritionist who needs to see the food items from the image
    and calculate the total calories, also provide the details of every food item with calories intake
    in the following format:

    1. Item 1 - no of calories
    2. Item 2 - no of calories
    ----
    ----
    """
    response_text = get_gemini_response(user_input, image_data, input_prompt)
    st.subheader("The Response is")
    st.write(response_text)
