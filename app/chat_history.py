import json
import os


CHAT_HISTORY_FILE = "logs/chat_history.json"

def save_chat_history(history):
    """Save chat history to a JSON file"""
    os.makedirs("logs", exist_ok=True)
    with open(CHAT_HISTORY_FILE, "w") as file:
        json.dump(history, file)

def load_chat_history():
    """Load chat history from a JSON file"""
    if os.path.exists(path=CHAT_HISTORY_FILE):
        with open(file=CHAT_HISTORY_FILE, mode='r') as file:
            return json.load(file)
    return []