from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text_into_chunks(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 100
) -> list[str]:
    if not text or not text.strip():
        raise ValueError("Input text is empty.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_text(text)

    if not chunks:
        raise ValueError("No chunks were created from the input text.")

    return chunks