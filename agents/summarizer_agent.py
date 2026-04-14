# agents/summarizer_agent.py

import os
from dotenv import load_dotenv
from openai import OpenAI

from utils.prompts import SUMMARIZER_AGENT_PROMPT


load_dotenv()


class SummarizerAgent:
    """
    Summarizer Agent:
    Summarizes the retrieved context.
    """

    def __init__(self, model: str = "gpt-4.1-mini"):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing in the .env file.")

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def run(self, context: str) -> str:
        """
        Generate a summary from retrieved context.

        Args:
            context (str): Retrieved context

        Returns:
            str: Summary text
        """
        if not context or not context.strip():
            return "No context available to summarize."

        response = self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": SUMMARIZER_AGENT_PROMPT
                },
                {
                    "role": "user",
                    "content": f"Summarize this context clearly:\n\n{context}"
                }
            ]
        )

        return response.output_text.strip()