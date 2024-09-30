# File: coordinator/rag.py

import ollama
import faiss
import numpy as np
from typing import List, Tuple, Optional


class RAGSystem:
    """
    Retrieval-Augmented Generation (RAG) system for enhancing query responses.

    This class implements a RAG system using FAISS for efficient similarity search
    and Ollama for text embedding and generation.

    Attributes:
        model (str): The name of the Ollama model to use.
        index (faiss.IndexFlatL2): FAISS index for similarity search.
        texts (List[str]): List of text documents corresponding to the index.
    """

    def __init__(self, index_path: str, texts_path: str, model_name: str = "mistral"):
        """
        Initialize the RAG system.

        Args:
            index_path (str): Path to the pre-computed FAISS index file.
            texts_path (str): Path to the file containing indexed texts.
            model_name (str, optional): Name of the Ollama model to use. Defaults to "mistral".

        Raises:
            FileNotFoundError: If the index or texts file is not found.
        """
        self.model = model_name
        try:
            self.index = faiss.read_index(index_path)
            with open(texts_path, "r", encoding="utf-8") as f:
                self.texts = f.read().split("\n===DOCUMENT SEPARATOR===\n")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Could not find index or texts file: {e}")

    def query(self, query: str, k: int = 5) -> List[Tuple[str, float]]:
        """
        Perform a similarity search for the given query.

        Args:
            query (str): The query string to search for.
            k (int, optional): The number of similar documents to retrieve. Defaults to 5.

        Returns:
            List[Tuple[str, float]]: A list of tuples containing the similar texts and their distances.
        """
        query_embedding = ollama.generate(model=self.model, prompt=f"Embed: {query}")
        distances, indices = self.index.search(np.array([query_embedding]), k)
        return [(self.texts[i], distances[0][j]) for j, i in enumerate(indices[0])]

    def generate_with_context(self, query: str) -> str:
        """
        Generate a response to the query using retrieved context.

        Args:
            query (str): The user's query.

        Returns:
            str: The generated response based on the query and retrieved context.
        """
        relevant_docs = self.query(query)
        context = "\n".join([doc for doc, _ in relevant_docs])
        response = ollama.generate(
            model=self.model, prompt=f"Context:\n{context}\n\nQuery: {query}"
        )
        return response


# Global RAG system instance
rag_system: Optional[RAGSystem] = None


def initialize_rag(index_path: str, texts_path: str, model_name: str = "mistral"):
    """
    Initialize the global RAG system.

    This function should be called before using rag_generate.

    Args:
        index_path (str): Path to the pre-computed FAISS index file.
        texts_path (str): Path to the file containing indexed texts.
        model_name (str, optional): Name of the Ollama model to use. Defaults to "mistral".

    Raises:
        FileNotFoundError: If the index or texts file is not found.
    """
    global rag_system
    rag_system = RAGSystem(index_path, texts_path, model_name)


def rag_generate(query: str) -> str:
    """
    Generate a response using the RAG system.

    This function should be called after initialize_rag has been called.

    Args:
        query (str): The user's query or prompt.

    Returns:
        str: The generated response based on retrieved context and the query.

    Raises:
        ValueError: If the RAG system has not been initialized.
    """
    if rag_system is None:
        raise ValueError("RAG system not initialized. Call initialize_rag first.")
    return rag_system.generate_with_context(query)
