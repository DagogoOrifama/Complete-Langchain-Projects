# AI-Powered Blog Generator with LLama 2 🤖

Welcome to the **AI-Powered Blog Generator with LLama 2** project! This repository demonstrates advanced capabilities in Generative AI and Large Language Models (LLM) by utilizing the powerful LLama 2 model to generate custom blog posts based on user input.


## Overview

This project is a Streamlit application designed to generate blog posts tailored to specific job profiles and topics. Users can input a topic, specify the desired word count, and select the target audience for the blog. The application then uses the LLama 2 model to generate a well-crafted blog post.

## Features

- **Custom Blog Generation**: Generate blogs based on specific needs by providing a topic, word count, and target audience.
- **Streamlit Interface**: A user-friendly interface built with Streamlit for easy interaction and blog generation.
- **Advanced AI Integration**: Leverages the LLama 2 model, showcasing advanced capabilities in Generative AI and LLM.

## How It Works

1. **Input the Blog Topic**: Enter the topic you want the blog to be about.
2. **Specify Word Count**: Specify the number of words for the blog post.
3. **Select Target Audience**: Choose the target audience from options such as Researchers, Data Scientists, and Common People.
4. **Generate Blog**: Click the "Generate" button to create a blog post based on the provided inputs using the LLama 2 model.

## Code Overview

The core functionality of this application is built around the `generate_blog_response` function, which interacts with the LLama 2 model to generate the blog content. Here's a brief overview of the key components:

### Function to Generate Blog Response

```python
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
    response = model.prompt.format(audience=audience, topic=topic, word_count=word_count)
    print(response)
    return response
  ```

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/generate-blogs-llama2.git
    ```
2. Navigate to the project directory:
    ```bash
    cd generate-blogs-llama2
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LLama 2 Model](https://github.com/facebookresearch/llama)

## Contact

For any questions or feedback, please reach out to:

**Dagogo**  
[dagoris2010@gmail.com](mailto:dagoris2010@gmail.com)

---

Thank you for checking out this project! Feel free to reach out if you have any questions or feedback.
