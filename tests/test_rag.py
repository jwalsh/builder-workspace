import pytest
from coordinator.rag import RAGSystem


@pytest.fixture
def rag_system():
    return RAGSystem("coordinator_docs.index", "coordinator_docs.texts")


def test_rag_query(rag_system):
    result = rag_system.query("What is Coordinator?")
    assert len(result) > 0
    assert any("Coordinator" in doc for doc, _ in result)


def test_generate_with_context(rag_system):
    response = rag_system.generate_with_context("What is Coordinator?")
    assert "project management" in response.lower() or "Coordinator" in response
