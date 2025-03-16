RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows you to upload PDF or Word documents, ask questions, and get answers based on the content of the documents. The chatbot uses DeepSeek 1.5B via Ollama for response generation and an ensemble retriever (semantic + BM25) for document retrieval.
Features

    Document Upload: Upload multiple PDF or Word documents.

    Chat Interface: Interactive chat interface built with Gradio.

    Local Execution: Runs entirely on your local machine.

    Chat History: Persists chat history in a JSON file.

    Docker Support: Containerized for easy deployment.

Prerequisites

    Python 3.9 or higher.

    Docker (optional, for containerized deployment).

    Ollama (for running DeepSeek 1.5B locally).

Installation
1. Clone the Repository
bash
Copy

git clone https://github.com/arjunjanamatti/advanced_rag.git
cd advanced_rag

2. Install Python Dependencies
bash
Copy

pip install -r requirements.txt

3. Set Up Ollama

    Install Ollama by following the instructions on the Ollama GitHub repository.

    Pull the DeepSeek 1.5B model:
    bash
    Copy

    ollama pull deepseek-1.5b

Running the Chatbot
Option 1: Run Locally

    Start the chatbot:
    bash
    Copy

    python app/main.py

    Open your browser and go to:
    Copy

    http://localhost:7860

Option 2: Run with Docker

    Build the Docker image:
    bash
    Copy

    docker build -t advanced_rag .

    Run the Docker container:
    bash
    Copy

    docker run -p 7860:7860 advanced_rag

    Open your browser and go to:
    Copy

    http://localhost:7860

Usage

    Upload Documents:

        Use the file uploader to upload one or more PDF or Word documents.

        The system will process the documents and make them available for retrieval.

    Ask Questions:

        Type your question in the chat input box.

        The chatbot will retrieve relevant information from the documents and generate a response.

    View Chat History:

        The chat history is saved in logs/chat_history.json.
