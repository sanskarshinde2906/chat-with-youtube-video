from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(
    text: str,
    chunk_size: int = 1800,
    chunk_overlap: int = 300,
) -> list[str]:
    """
    Split transcript into overlapping text chunks using
    LangChain's RecursiveCharacterTextSplitter.

    Args:
        text (str): Full transcript.
        chunk_size (int): Maximum characters per chunk.
        chunk_overlap (int): Overlap between consecutive chunks.

    Returns:
        list[str]: List of text chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            " ",
            "",
        ],
    )

    chunks = splitter.split_text(text)

    return chunks


