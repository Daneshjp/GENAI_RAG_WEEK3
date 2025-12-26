from dotenv import load_dotenv
load_dotenv()

from ingestion import load_documents
from splitter import split_documents
from vector_store import create_vector_store
from retriever import retrieve_chunks
from llm_answer import generate_answer
from embeddings import get_embedding_model


if __name__ == "__main__":

    # -------------------------
    # PHASE 1: INGESTION
    # -------------------------
    docs = load_documents("data")
    print(f"\nLoaded {len(docs)} documents")

    # -------------------------
    # PHASE 2: CHUNKING
    # -------------------------
    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks")


    # -------------------------
    # PHASE 3: EMBEDDINGS
    # -------------------------
    embeddings = get_embedding_model()

    # -------------------------
    # PHASE 4: VECTOR STORE
    # -------------------------
    vectordb = create_vector_store(chunks, embeddings)
    print("Vector store created")
    print("vectordb type:", type(vectordb))

    # -------------------------
    # PHASE 5: RETRIEVAL
    # -------------------------
    query = "Who was Rani Lakshmibai?"
    print(f"\nQuery: {query}")

    print("DEBUG vectordb value:", vectordb)
    print("DEBUG vectordb type:", type(vectordb))


    retrieved_docs = retrieve_chunks(query, vectordb, k=3)

    print("\nTop Results:\n")
    for i, doc in enumerate(retrieved_docs, 1):
        print(f"Result {i}")
        print(doc.page_content)
        print("-" * 80)

    # -------------------------
    # PHASE 6: RAG + LLM ANSWER
    # -------------------------
    final_answer = generate_answer(query, retrieved_docs)

    print("\n--- FINAL RAG ANSWER ---")
    print(final_answer)
