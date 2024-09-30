# File: coordinator/indexer.py

import os
from typing import List, Tuple
from bs4 import BeautifulSoup
import faiss
import numpy as np
import ollama


def extract_text_from_html(file_path: str) -> str:
    """
    Extract plain text content from an HTML file.

    Args:
        file_path (str): Path to the HTML file.

    Returns:
        str: Extracted text content.

    Raises:
        FileNotFoundError: If the specified file is not found.
        IOError: If there's an error reading the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            return soup.get_text()
    except FileNotFoundError:
        raise FileNotFoundError(f"HTML file not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {str(e)}")


def create_embeddings(texts: List[str], model: str = "mistral") -> np.ndarray:
    """
    Create embeddings for a list of texts using the specified Ollama model.

    Args:
        texts (List[str]): List of text strings to embed.
        model (str, optional): Name of the Ollama model to use. Defaults to 'mistral'.

    Returns:
        np.ndarray: Array of embeddings.
    """
    embeddings = []
    for text in texts:
        embedding = ollama.generate(model=model, prompt=f"Embed: {text[:1000]}")
        embeddings.append(embedding)
    return np.array(embeddings)


def create_index(
    docs_dir: str, model: str = "mistral"
) -> Tuple[faiss.IndexFlatL2, List[str]]:
    """
    Create a FAISS index from HTML documentation files.

    Args:
        docs_dir (str): Directory containing HTML documentation files.
        model (str, optional): Name of the Ollama model to use for embeddings. Defaults to 'mistral'.

    Returns:
        Tuple[faiss.IndexFlatL2, List[str]]: A tuple containing the FAISS index and a list of processed texts.

    Raises:
        ValueError: If no HTML files are found in the specified directory.
    """
    texts = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                text = extract_text_from_html(file_path)
                texts.append(text)

    if not texts:
        raise ValueError(f"No HTML files found in directory: {docs_dir}")

    embeddings = create_embeddings(texts, model)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index, texts


def save_index_and_texts(
    index: faiss.IndexFlatL2, texts: List[str], index_path: str, texts_path: str
):
    """
    Save the FAISS index and processed texts to files.

    Args:
        index (faiss.IndexFlatL2): The FAISS index to save.
        texts (List[str]): List of processed texts to save.
        index_path (str): Path where the index should be saved.
        texts_path (str): Path where the texts should be saved.

    Raises:
        IOError: If there's an error writing the files.
    """
    try:
        faiss.write_index(index, index_path)
        with open(texts_path, "w", encoding="utf-8") as f:
            f.write("\n===DOCUMENT SEPARATOR===\n".join(texts))
    except IOError as e:
        raise IOError(f"Error saving index or texts: {str(e)}")


def build_rag_index(
    docs_dir: str, index_path: str, texts_path: str, model: str = "mistral"
):
    """
    Build and save a RAG index from documentation files.

    This function processes HTML files in the specified directory, creates embeddings,
    builds a FAISS index, and saves both the index and processed texts.

    Args:
        docs_dir (str): Directory containing HTML documentation files.
        index_path (str): Path where the FAISS index should be saved.
        texts_path (str): Path where the processed texts should be saved.
        model (str, optional): Name of the Ollama model to use for embeddings. Defaults to 'mistral'.

    Raises:
        ValueError: If no HTML files are found in the specified directory.
        IOError: If there's an error reading input files or writing output files.
    """
    print(f"Processing documentation in {docs_dir}...")
    index, texts = create_index(docs_dir, model)

    print(f"Saving index to {index_path} and texts to {texts_path}...")
    save_index_and_texts(index, texts, index_path, texts_path)

    print("RAG index built and saved successfully.")


if __name__ == "__main__":
    # Example usage
    docs_directory = "docs/_build/html"
    index_output = "coordinator_docs.index"
    texts_output = "coordinator_docs.texts"

    build_rag_index(docs_directory, index_output, texts_output)
