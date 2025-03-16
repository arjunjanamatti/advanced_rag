import gradio as gr
from document_loader import load_documents
from chunker import chunk_text
from retreiver import build_retrievers, ensemble_retrieve
from generator import generate_response
from chat_history import save_chat_history, load_chat_history

# Global variables
chunks = []
bm25 = None

def process_uploaded_files(files):
    """Process uploaded files and update the knowledge base."""
    global chunks, bm25
    file_paths = [file.name for file in files]
    text = load_documents(file_paths)
    chunks = chunk_text(text)
    bm25 = build_retrievers(chunks)

def chatbot(query, history):
    """Handle chatbot interactions."""
    global chunks, bm25
    if not chunks or not bm25:
        return history, history  # No documents uploaded yet

    # Retrieve relevant chunks
    relevant_chunks = ensemble_retrieve(query, bm25)

    # Generate response
    response = generate_response(query, relevant_chunks)

    # Update chat history
    history.append((query, response))
    save_chat_history(history)
    return history, history

# Load chat history
chat_history = load_chat_history()

# Gradio interface
with gr.Blocks() as demo:
    file_upload = gr.File(file_count="multiple", label="Upload Documents")
    chatbot_interface = gr.Chatbot(label="Chatbot", value=chat_history)
    query_input = gr.Textbox(label="Your Question")
    submit_button = gr.Button("Submit")

    file_upload.change(process_uploaded_files, inputs=file_upload, outputs=[])
    submit_button.click(chatbot, inputs=[query_input, chatbot_interface], outputs=[chatbot_interface, chatbot_interface])

demo.launch()