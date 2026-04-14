# agents/qa_agent.py

import os
from dotenv import load_dotenv
from openai import OpenAI

from utils.prompts import QA_AGENT_PROMPT


load_dotenv()


class QAAgent:
    """
    Q&A Agent:
    Answers the user's question using the retrieved context.
    """

    def __init__(self, model: str = "gpt-4.1-mini"):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing in the .env file.")

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def run(self, context: str, user_question: str) -> str:
        """
        Answer the user's question using only the provided context.

        Args:
            context (str): Retrieved context
            user_question (str): User's question

        Returns:
            str: Answer
        """
        if not context or not context.strip():
            return "No context is available to answer the question."

        if not user_question or not user_question.strip():
            return "No user question was provided."

        response = self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": QA_AGENT_PROMPT
                },
                {
                    "role": "user",
                    "content": (
                        f"Context:\n{context}\n\n"
                        f"User Question:\n{user_question}\n\n"
                        "Answer the question using only the provided context."
                    )
                }
            ]
        )

        return response.output_text.strip()