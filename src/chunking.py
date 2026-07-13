import nltk
from nltk.tokenize import sent_tokenize

# Run only once
nltk.download("punkt")


def split_into_sentences(text: str) -> list[str]:
    """
    Convert transcript into a list of sentences.
    """
    return sent_tokenize(text)


def create_chunks(
    sentences: list[str],
    chunk_size: int = 15,
    overlap: int = 3
) -> list[str]:
    """
    Create sentence-based chunks with overlap.

    Args:
        sentences (list[str]): List of sentences.
        chunk_size (int): Number of sentences per chunk.
        overlap (int): Number of overlapping sentences.

    Returns:
        list[str]: List of text chunks.
    """

    if overlap >= chunk_size:
        raise ValueError(
            "Overlap must be smaller than chunk_size."
        )

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(sentences), step):

        chunk = sentences[i:i + chunk_size]

        chunks.append(" ".join(chunk))

    return chunks


if __name__ == "__main__":

    text = """
    Sentence 1.
    Sentence 2.
    Sentence 3.
    Sentence 4.
    Sentence 5.
    Sentence 6.
    Sentence 7.
    Sentence 8.
    Sentence 9.
    Sentence 10.
    Sentence 11.
    Sentence 12.
    Sentence 13.
    Sentence 14.
    Sentence 15.
    Sentence 16.
    Sentence 17.
    Sentence 18.
    Sentence 19.
    Sentence 20.
    """

    sentences = split_into_sentences(text)

    chunks = create_chunks(
        sentences,
        chunk_size=30,
        overlap=5
    )

    for index, chunk in enumerate(chunks, start=1):

        print(f"\nChunk {index}\n")

        print(chunk)
