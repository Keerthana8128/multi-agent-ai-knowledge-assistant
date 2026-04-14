# agents/retriever_agent.py

from typing import List


class RetrieverAgent:
    """
    Retriever Agent:
    Selects and formats the most relevant retrieved chunks.
    """

    def run(self, retrieved_chunks: List[str]) -> str:
        """
        Combine retrieved chunks into a readable context block.

        Args:
            retrieved_chunks (List[str]): Retrieved text chunks

        Returns:
            str: Formatted relevant context
        """
        if not retrieved_chunks:
            return "No relevant context was retrieved."

        formatted_chunks = []
        for index, chunk in enumerate(retrieved_chunks, start=1):
            formatted_chunks.append(f"Context {index}:\n{chunk}")

        return "\n\n".join(formatted_chunks)