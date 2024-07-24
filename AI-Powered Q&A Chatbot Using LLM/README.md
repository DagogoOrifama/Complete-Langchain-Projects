# Q&A Chatbot

This project is a Q&A chatbot application that leverages advanced language models to provide intelligent and coherent responses to user queries. The application is built using Streamlit and integrates the LangChain library to facilitate communication with OpenAI's models.

## Features

- **Conversational Interface**: Engages users in a natural conversation using a text input interface.
- **AI-Powered Responses**: Utilizes OpenAI's language models to generate human-like responses.
- **User-Friendly Interface**: Simple and intuitive interface built with Streamlit.

## How It Works

1. **User Interaction**: Users input their questions through a text box in the Streamlit interface.
2. **AI Response Generation**: The application sends the user input to OpenAI's language model and receives a response.
3. **Display Response**: The response is displayed below the input box for the user to read.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up your environment variables**:
    - Create a `.env` file in the root directory of the project.
    - Add your OpenAI API key:
      ```env
      OPENAI_API_KEY=your_openai_api_key
      ```

4. **Run the application**:
    ```sh
    streamlit run app.py
    ```

## Usage

1. **Open the application**:
    Once the application is running, open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

2. **Start a Conversation**:
    - Enter your question in the text input box.
    - Click the "Ask the question" button to submit your query.
    - The application will display the AI's response below the input box.

## Dependencies

The project requires the following Python packages:

- `langchain`
- `openai`
- `huggingface_hub`
- `python-dotenv`
- `streamlit`

Make sure to install these dependencies using the provided `requirements.txt` file.

## License

This project is licensed under the MIT License. See the **LICENSE** file for details.
