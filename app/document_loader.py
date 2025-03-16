import os
from PyPDF2 import PdfReader
from docx import Document

def load_pdf(file_path):
    '''Load text from a pdf file'''
    with open(file=file_path, mode='rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    return text

def load_word(file_path):
    '''Load text from a Word file'''
    doc = Document(file_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def chunk_text(text, chunk_size = 300, overlap=50):
    """
    Split text into smaller chunks with optional overlap
    :param text: Input text to chunk
    :param chunk_size: Maximum number of words per chunk
    :param overlap: Number of overlapping words between chunks
    :return List of chunks
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size-overlap):
        chunk = ' '.join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def load_and_chunk_documents(file_paths, chunk_size = 300, overlap=50):
    """
    Load and chunk multiple documents
    :param file_paths: List of file paths (PDF or Word)
    :param chunk_size: Maximum number of words per chunk
    :param overlap: Number of overlapping words between chunks
    :return List of chunks
    """
    text = ''
    for file_path in file_paths:
        if file_path.endswith(".pdf"):
            text += load_pdf(file_path=file_path)
        elif file_path.endswith(".docx"):
            text += load_word(file_path=file_path)
    return chunk_text(text=text)