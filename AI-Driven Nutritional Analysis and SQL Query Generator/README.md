# AI-Driven Nutritional Analysis and SQL Query Generator

This project is a Q&A Chatbot application that leverages the power of Google's Gemini model, a large language model (LLM) capable of multimodal analysis, to analyze images and provide detailed nutritional information. Additionally, it includes a module to convert natural language questions into SQL queries. The application is built using Streamlit and allows users to upload an image, input a prompt, and receive a response detailing the nutritional content of the food items in the image or SQL query results based on user questions.

## Features

- **Image Upload**: Users can upload images in JPG, JPEG, or PNG formats.
- **Input Prompt**: Users can input a custom prompt to tailor the response.
- **Nutritional Analysis**: The application uses a multimodal LLM to analyze the uploaded image and provide detailed information about the food items present, including their caloric content.
- **SQL Query Generator**: Converts natural language questions into SQL queries and retrieves data from a SQLite database.

## How It Works

### Nutritional Analysis

The application integrates Google's Gemini model through the `google-generativeai` library. This model is a state-of-the-art large language model capable of understanding and generating text based on image inputs. It performs the following steps:

1. **Image Upload**: The user uploads an image containing food items.
2. **Prompt Input**: The user provides a custom prompt to specify the type of analysis required.
3. **Image and Prompt Processing**: The Gemini model processes the image and the prompt to generate a response.
4. **Nutritional Analysis**: The model outputs a detailed nutritional analysis of the food items present in the image.

### SQL Query Generator

1. **Question Input**: The user inputs a question in natural language.
2. **Prompt Input**: A predefined prompt helps the Gemini model understand the context.
3. **Query Processing**: The Gemini model converts the question into an SQL query.
4. **SQL Execution**: The query is executed on a SQLite database and the results are displayed.

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
    - Add your Google API key:
      ```env
      GOOGLE_API_KEY=your_google_api_key
      ```

4. **Run the application**:
    ```sh
    streamlit run app.py
    ```

## Usage

### Nutritional Analysis

1. **Open the application**:
    Once the application is running, open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

2. **Upload an Image**:
    - Click on the "Choose an image..." button to upload your image.
    - The supported formats are JPG, JPEG, and PNG.

3. **Input Prompt**:
    - Enter your custom prompt in the "Input Prompt" text box.

4. **Submit**:
    - Click the "Tell me about the image" button.
    - The application will display the uploaded image and provide a detailed response about the nutritional content.

### SQL Query Generator

1. **Open the SQL Query Generator**:
    - Navigate to the appropriate section in the application.

2. **Input Question**:
    - Enter your question in the "Input" text box.

3. **Submit**:
    - Click the "Ask the question" button.
    - The application will display the SQL query results.

## Dependencies

The project requires the following Python packages:

- `streamlit==1.10.0`
- `google-generativeai==0.0.2`
- `python-dotenv==0.19.2`
- `langchain==0.5.0`
- `PyPDF2==1.26.0`
- `chromadb==0.1.1`
- `faiss-cpu==1.7.1`
- `pdf2image==1.16.0`
- `sqlite3==2.6.0`

Make sure to install these dependencies using the provided `requirements.txt` file.

## License

This project is licensed under the MIT License. See the **LICENSE** file for details.
