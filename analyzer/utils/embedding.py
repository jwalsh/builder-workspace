import requests


def get_embedding(text):
    url = "http://localhost:11434/api/embeddings"
    payload = {"model": "mxbai-embed-large", "prompt": text}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["embedding"]
