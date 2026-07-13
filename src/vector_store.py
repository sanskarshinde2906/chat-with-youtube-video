import faiss


def create_index(embeddings):
    """
    Create a FAISS index and add embeddings.

    Parameters
    ----------
    embeddings : numpy.ndarray
        Shape -> (number_of_chunks, embedding_dimension)

    Returns
    -------
    faiss.IndexFlatL2
    """

    # Get embedding dimension
    dimension = embeddings.shape[1]

    # Create empty FAISS index
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings to index
    index.add(embeddings)

    return index


def search_index(index, query_embedding, top_k=3):
    """
    Search top-k similar vectors.

    Parameters
    ----------
    index : faiss.IndexFlatL2

    query_embedding : numpy.ndarray
        Shape -> (1, embedding_dimension)

    top_k : int

    Returns
    -------
    distances, indices
    """

    distances, indices = index.search(query_embedding, top_k)

    return distances, indices





