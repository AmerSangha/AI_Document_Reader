from flask import Flask, request, render_template, jsonify
from transformers import pipeline
import PyPDF2
import docx

app = Flask(__name__)

# Use separate models for summarization and generative question-answering
summarizer_model_id = "facebook/bart-large-cnn"
qa_model_id = "google/flan-t5-small"  # A model for generative QA

# Load the models
summarizer = pipeline("summarization", model=summarizer_model_id)
qa_model = pipeline("text2text-generation", model=qa_model_id)  # Updated to use generative QA model


# Function to read .docx files
def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


# Function to read .pdf files
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']

    if file.filename.endswith('.pdf'):
        text = read_pdf(file)
    elif file.filename.endswith('.docx'):
        text = read_docx(file)
    else:
        return "Unsupported file type", 400

    # Generate summary using the summarization model
    summary = summarizer(text, max_length=500, min_length=30, do_sample=False)

    # Render the summary and allow interaction
    return render_template('result.html', summary=summary[0]['summary_text'])


# New route for handling chat questions
@app.route('/ask', methods=['POST'])
def ask_question():
    user_question = request.json['question']  # Get the user's question from the request
    summary_text = request.json['summary']    # Pass the summary to the QA model

    # Use the generative QA model
    input_text = f"Question: {user_question} Context: {summary_text}"  # Create input for the model
    response = qa_model(input_text, max_length=100)  # Get the response from the model

    return jsonify({'answer': response[0]['generated_text']})  # Return the generative answer as JSON


if __name__ == '__main__':
    app.run(debug=True)
