def create_chunks(
    text: str,
    chunk_size: int = 1800,
    overlap: int = 300
) -> list[str]:
    """
    Split transcript into character-based chunks with overlap.

    Args:
        text (str): Full transcript.
        chunk_size (int): Maximum characters in one chunk.
        overlap (int): Number of overlapping characters.

    Returns:
        list[str]: List of text chunks.
    """

    if overlap >= chunk_size:
        raise ValueError(
            "Overlap must be smaller than chunk_size."
        )

    chunks = []

    start = 0

    while start < len(text):

        end = min(start + chunk_size, len(text))

        # Avoid cutting words in the middle
        if end < len(text):

            while end > start and text[end] != " ":
                end -= 1

        chunk = text[start:end].strip()

        chunks.append(chunk)

        start = end - overlap

    return chunks


