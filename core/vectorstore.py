# core/vectorstore.py

from langchain_community.vectorstores import FAISS


def create_faiss_vectorstore(chunks: list[str], embedding_model):
    """
    Create a FAISS vector store from text chunks.

    Args:
        chunks (list[str]): List of text chunks
        embedding_model: Embedding model instance

    Returns:
        FAISS: Vector store
    """
    if not chunks:
        raise ValueError("Chunks list is empty.")

    return FAISS.from_texts(chunks, embedding_model)


def retrieve_relevant_chunks(vectorstore, user_question: str, k: int = 3) -> list[str]:
    """
    Retrieve top-k relevant chunks for a user question.

    Args:
        vectorstore: FAISS vector store
        user_question (str): User query
        k (int): Number of chunks to retrieve

    Returns:
        list[str]: Relevant chunk texts
    """
    if not user_question or not user_question.strip():
        raise ValueError("User question is empty.")

    docs = vectorstore.similarity_search(user_question, k=k)
    return [doc.page_content for doc in docs]