# Chat with PDF using Gemini

This project is an innovative application that allows users to interact with PDF documents using natural language queries. The application leverages Google's Gemini model and other advanced technologies to extract, process, and query text from PDF files.

## Features

- **PDF Text Extraction**: Upload multiple PDF documents and extract their text content.
- **Text Chunking**: Split the extracted text into manageable chunks for processing.
- **Vector Store Creation**: Create a vector store using Google Generative AI embeddings for efficient text search and retrieval.
- **Conversational Chain**: Use a conversational chain to answer user queries based on the PDF content.
- **User-Friendly Interface**: Simple and intuitive interface built with Streamlit.

## How It Works

1. **Upload PDFs**: Users can upload multiple PDF files through the Streamlit interface.
2. **Process PDFs**: The application extracts text from the PDFs, splits the text into chunks, and creates a vector store for efficient querying.
3. **Ask Questions**: Users can input natural language questions, and the application uses the vector store and conversational chain to provide accurate answers based on the PDF content.

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
    streamlit run chatpdf1.py
    ```

## Usage

1. **Open the application**:
    Once the application is running, open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

2. **Upload PDF Files**:
    - Use the sidebar menu to upload your PDF files.
    - Click on the "Submit & Process" button to process the uploaded PDFs.

3. **Ask Questions**:
    - Enter your question in the text input box on the main page.
    - The application will provide a detailed answer based on the content of the uploaded PDFs.

## Dependencies

The project requires the following Python packages:

- `streamlit`
- `google-generativeai`
- `python-dotenv`
- `langchain`
- `PyPDF2`
- `chromadb`
- `faiss-cpu`
- `langchain_google_genai`

Make sure to install these dependencies using the provided `requirements.txt` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
