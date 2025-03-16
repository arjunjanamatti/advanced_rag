from sentence_transformers import SentenceTransformer
import faiss
from rank_bm25 import BM25Okapi
import numpy as np


# load a pre-trained embedding model
model = SentenceTransformer(model_name_or_path="all-MiniLM-L6-v2")

# create FAISS index (facebook AI similarity search)
dimension = 384 # Dimension of the embedding model
index = faiss.IndexFlatL2(dimension)

def build_retreivers(chunks):
    """Build semantic and BM25 retrievers"""
    # Semantic retriever
    chunk_embeddings = model.encode(chunks)
    index.add(n=chunk_embeddings)

    # BM25 retriever
    tokenized_chunks = [chunk.split() for chunk in chunks]
    bm25 = BM25Okapi(corpus=tokenized_chunks)
    return bm25

def ensemble_retrieve(chunks, query, bm25, top_k = 3):
    """Retrieve relevant chunks using ensemble retrieval"""
    # semantic search
    query_embedding = model.encode(sentences=[query])
    distances, semantic_indexes = index.search(n=query_embedding, x=top_k)
    semantic_results = [chunks[i] for i in semantic_indexes[0]]

    # BM25 search
    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)
    bm25_indices = np.argsort(bm25_scores)[-top_k:][::-1]
    bm25_results = [chunks[i] for i in bm25_indices]

    # combine results
    combined_results = list(set(semantic_results + bm25_results))
    return combined_results[:top_k]
