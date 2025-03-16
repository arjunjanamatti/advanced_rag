import ollama

def generate_response(query, chunks):
    """
    Generate a response using DeepSeek 1.5B via Ollama.
    :param query: User's question.
    :param chunks: Retrieved chunks of text.
    :return: Generated response.
    """
    # Combine chunks into a single context
    context = " ".join(chunks)

    # Create the prompt for the model
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"

    # Generate response using Ollama
    response = ollama.generate(
        model="deepseek-r1:1.5b",  # Replace with the correct model name in Ollama
        prompt=prompt,
        options={
            "max_tokens": 200,  # Adjust as needed
            "temperature": 0.7,  # Adjust for creativity
            "top_p": 0.95,       # Adjust for diversity
        }
    )

    # Return the generated response
    return response['response']