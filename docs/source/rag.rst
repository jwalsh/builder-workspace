# File: docs/source/rag.rst

RAG (Retrieval-Augmented Generation)
====================================

The RAG system enhances the Coordinator's response generation by leveraging a pre-computed index of relevant documentation.

Functions
---------

.. automodule:: coordinator.rag
   :members:
   :undoc-members:
   :show-inheritance:

Usage
-----

To use the RAG system in your project:

1. Initialize the RAG system:

   .. code-block:: python

      from coordinator.rag import initialize_rag
      
      initialize_rag("path/to/index.faiss", "path/to/texts.txt")

2. Generate responses using RAG:

   .. code-block:: python

      from coordinator.rag import rag_generate
      
      response = rag_generate("Your query here")

Make sure to initialize the RAG system before generating responses.
