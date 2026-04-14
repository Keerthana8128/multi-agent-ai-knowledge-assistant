# core/orchestrator.py

from core.loader import load_pasted_text, load_text_file
from core.splitter import split_text_into_chunks
from core.embeddings import get_embedding_model
from core.vectorstore import create_faiss_vectorstore, retrieve_relevant_chunks

from agents.retriever_agent import RetrieverAgent
from agents.summarizer_agent import SummarizerAgent
from agents.qa_agent import QAAgent
from agents.recommendation_agent import RecommendationAgent


class MultiAgentOrchestrator:
    """
    Orchestrates the full multi-agent knowledge assistant workflow.
    """

    def __init__(self):
        self.retriever_agent = RetrieverAgent()
        self.summarizer_agent = SummarizerAgent()
        self.qa_agent = QAAgent()
        self.recommendation_agent = RecommendationAgent()

    def process_text(self, input_text: str, user_question: str) -> dict:
        """
        Process pasted text through the full pipeline.

        Args:
            input_text (str): User-provided text
            user_question (str): User question

        Returns:
            dict: Results from all agents
        """
        clean_text = load_pasted_text(input_text)
        return self._run_pipeline(clean_text, user_question)

    def process_file(self, file_path: str, user_question: str) -> dict:
        """
        Process a text file through the full pipeline.

        Args:
            file_path (str): Path to the input .txt file
            user_question (str): User question

        Returns:
            dict: Results from all agents
        """
        file_text = load_text_file(file_path)
        return self._run_pipeline(file_text, user_question)

    def _run_pipeline(self, text: str, user_question: str) -> dict:
        """
        Internal pipeline for chunking, retrieval, summarization, Q&A, and recommendations.

        Args:
            text (str): Input knowledge text
            user_question (str): User question

        Returns:
            dict: Pipeline outputs
        """
        chunks = split_text_into_chunks(text)
        embedding_model = get_embedding_model()
        vectorstore = create_faiss_vectorstore(chunks, embedding_model)

        retrieved_chunks = retrieve_relevant_chunks(vectorstore, user_question, k=3)
        retrieved_context = self.retriever_agent.run(retrieved_chunks)

        summary = self.summarizer_agent.run(retrieved_context)
        answer = self.qa_agent.run(retrieved_context, user_question)
        recommendations = self.recommendation_agent.run(
            retrieved_context,
            summary,
            answer
        )

        return {
            "chunks": chunks,
            "retrieved_chunks": retrieved_chunks,
            "retrieved_context": retrieved_context,
            "summary": summary,
            "answer": answer,
            "recommendations": recommendations,
        }