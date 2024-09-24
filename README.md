# AI_Document_Reader
This project is an AI-powered web application designed to read and summarize documents (PDF and DOCX formats) using natural language processing models. Users can upload a document, receive a summary, and ask questions about the content interactively.

AI Document Reader

This project is an AI-powered web application designed to read and summarize documents (PDF and DOCX formats) using natural language processing models. Users can upload a document, receive a summary, and ask questions about the content interactively.

Features
    Upload PDF or DOCX files.
    Generate a summary of the uploaded document.
    Ask questions about the summarized text.
    Interactive chat interface for user queries.

Technologies Used
    Flask: Web framework for Python.
    Transformers: Hugging Face library for state-of-the-art NLP models.
    PyPDF2: For reading PDF files.
    python-docx: For reading DOCX files.

Installation
  Clone the repository:
    git clone <repository-url>
    cd AI_Document_Reader

  Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

  Install the required packages:
    pip install -r requirements.txt

Usage

    Run the Flask application:
      python app.py
      Open your web browser and go to http://127.0.0.1:5000/.
      Upload a PDF or DOCX file.
      Wait for the summary to load (this may take around 30 seconds, depending on the file size and your system performance).
      Ask questions about the summarized text in the chat interface.

Limitations

The summarization and generative question-answering models are designed to work on smaller documents. This application is not meant for large documents, as the AI models and the system may struggle to handle extensive information.
    The generative question-answering model may provide limited responses, primarily suited for basic queries regarding the summarized text.

Disclaimer

This application is a proof of concept. As such, the performance of the AI models and the overall system is not optimized for production use. The development server should not be used in a production deployment.
