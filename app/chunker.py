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
