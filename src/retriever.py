from vector_store import search_index


def retrieve_chunks(index, query_embedding, chunks, top_k=3):
    """
    Retrieve the most relevant chunks from the FAISS index.

    Parameters
    ----------
    index : faiss.Index
        FAISS index containing chunk embeddings.

    query_embedding : numpy.ndarray
        Embedding of the user's question.

    chunks : list[str]
        Original text chunks.

    top_k : int, optional
        Number of chunks to retrieve. Default is 3.

    Returns
    -------
    list[str]
        List of retrieved text chunks.
    """

    # Search the FAISS index
    distances, indices = search_index(
        index=index,
        query_embedding=query_embedding,
        top_k=top_k
    )

    # Retrieve original chunks
    retrieved_chunks = []

    for i in indices[0]:
        retrieved_chunks.append(chunks[i])

    return retrieved_chunks