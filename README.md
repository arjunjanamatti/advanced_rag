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

git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot

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

    docker build -t rag-chatbot .

    Run the Docker container:
    bash
    Copy

    docker run -p 7860:7860 rag-chatbot

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

Project Structure
Copy

rag-chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main application logic
│   ├── document_loader.py   # Load and process PDF/Word docs
│   ├── chunker.py           # Chunking logic
│   ├── retriever.py         # Ensemble retriever (semantic + BM25)
│   ├── generator.py         # DeepSeek 1.5B-based response generation
│   ├── chat_history.py      # Save and load chat history
│   └── utils.py            # Utility functions
├── data/                   # Folder for uploaded documents
├── logs/                   # Folder for chat history logs
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignore files for Git

Docker Compose (Optional)

If you prefer using Docker Compose, create a docker-compose.yml file:
yaml
Copy

version: "3.8"
services:
  rag-chatbot:
    build: .
    ports:
      - "7860:7860"
    volumes:
      - ./logs:/app/logs

Then run:
bash
Copy

docker-compose up

Troubleshooting

    Docker Desktop Not Starting:

        Ensure WSL 2 is enabled. Open PowerShell as Administrator and run:
        bash
        Copy

        wsl --set-default-version 2

        Restart Docker Desktop.

    Port Conflict:

        If port 7860 is already in use, change the port mapping:
        bash
        Copy

        docker run -p 7870:7860 rag-chatbot

        Access the chatbot at http://localhost:7870.

    File Upload Issues:

        Ensure the data folder exists in the project directory.

        If using Docker volumes, ensure the correct path is provided.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

    DeepSeek: For the 1.5B language model.

    Ollama: For providing an easy way to run local models.

    Gradio: For the chatbot interface.