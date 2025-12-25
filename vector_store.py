from langchain_community.vectorstores import Chroma
from embeddings import get_embedding_model


def create_vector_store(chunks, persist_dir="chroma_db"):
    embedding = get_embedding_model()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=persist_dir
    )

    vectordb.persist()
    return vectordb
