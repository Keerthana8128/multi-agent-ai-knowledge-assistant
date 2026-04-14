# agents/recommendation_agent.py

import os
from dotenv import load_dotenv
from openai import OpenAI

from utils.prompts import RECOMMENDATION_AGENT_PROMPT


load_dotenv()


class RecommendationAgent:
    """
    Recommendation Agent:
    Suggests next actions based on context, summary, and answer.
    """

    def __init__(self, model: str = "gpt-4.1-mini"):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing in the .env file.")

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def run(self, context: str, summary: str, answer: str) -> str:
        """
        Generate next-step recommendations.

        Args:
            context (str): Retrieved context
            summary (str): Summary from summarizer agent
            answer (str): Answer from QA agent

        Returns:
            str: Recommended next actions
        """
        if not context or not context.strip():
            return "- No recommendations available because context is missing."

        response = self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": RECOMMENDATION_AGENT_PROMPT
                },
                {
                    "role": "user",
                    "content": (
                        f"Context:\n{context}\n\n"
                        f"Summary:\n{summary}\n\n"
                        f"Answer:\n{answer}\n\n"
                        "Suggest 3 practical next actions."
                    )
                }
            ]
        )

        return response.output_text.strip()