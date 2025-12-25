def retrieve_chunks(vectordb, query, k=3):
    return vectordb.similarity_search(query, k=k)
