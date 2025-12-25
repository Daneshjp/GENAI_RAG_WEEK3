from dotenv import load_dotenv
load_dotenv()

from ingestion import load_documents
from splitter import split_documents
from vector_store import create_vector_store
from retriever import retrieve_chunks


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
    # PHASE 3 & 4: EMBEDDINGS + VECTOR STORE
    # -------------------------
    vectordb = create_vector_store(chunks)
    print("Vector store created")

    # -------------------------
    # PHASE 5: RETRIEVAL
    # -------------------------
    query = "Who was Rani Lakshmibai?"
    results = retrieve_chunks(vectordb, query)

    print(f"\nQuery: {query}")
    print("\nTop Results:")
    for i, doc in enumerate(results, start=1):
        print(f"\nResult {i}")
        print(doc.page_content[:300])
