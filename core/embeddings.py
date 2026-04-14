import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()


def get_embedding_model() -> OpenAIEmbeddings:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing in the .env file.")

    return OpenAIEmbeddings(api_key=api_key)