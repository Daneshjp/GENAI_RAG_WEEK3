def retrieve_chunks(query, vectorstore, k=3):
    """
    vectorstore must be a Chroma object
    """
    return vectorstore.similarity_search(query, k=k)
