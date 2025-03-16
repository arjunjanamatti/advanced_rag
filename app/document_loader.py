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

def load_documents(file_paths):
    '''Load and concatenate text from multiple PDF/Word documents'''
    text = ''
    for file_path in file_paths:
        if file_path.endswith(".pdf"):
            text += load_pdf(file_path=file_path)
        elif file_path.endswith('.docx'):
            text += load_word(file_path=file_path)
    return text