# core/loader.py

from pathlib import Path


def load_text_file(file_path: str) -> str:
    """
    Load text content from a .txt file.

    Args:
        file_path (str): Path to the text file

    Returns:
        str: File content as text
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("Only .txt files are supported in version 1.")

    content = path.read_text(encoding="utf-8").strip()

    if not content:
        raise ValueError("The file is empty.")

    return content


def load_pasted_text(text: str) -> str:
    """
    Validate and return pasted text.

    Args:
        text (str): User pasted text

    Returns:
        str: Cleaned text
    """
    if not text or not text.strip():
        raise ValueError("No pasted text provided.")

    return text.strip()