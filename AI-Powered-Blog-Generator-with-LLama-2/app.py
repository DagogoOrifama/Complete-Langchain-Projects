import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def generate_blog_response(topic, word_count, audience):
    # Configure the LLama 2 model
    model = CTransformers(
        model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={'max_new_tokens': 256, 'temperature': 0.01}
    )

    # Define the prompt template
    prompt_text = """
        Write a blog for {audience} job profile for a topic {topic}
        within {word_count} words.
    """

    prompt = PromptTemplate(
        input_variables=["audience", "topic", "word_count"],
        template=prompt_text
    )

    # Generate the response from the LLama 2 model
    response = model(prompt.format(audience=audience, topic=topic, word_count=word_count))
    print(response)
    return response

# Configure the Streamlit app
st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Blogs 🤖")

# User inputs for blog topic, word count, and audience
blog_topic = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns(2)

with col1:
    word_count = st.text_input('No of Words')
with col2:
    audience = st.selectbox('Writing the blog for', ['Researchers', 'Data Scientist', 'Common People'], index=0)

# Button to trigger blog generation
if st.button("Generate"):
    result = generate_blog_response(blog_topic, word_count, audience)
    st.write(result)