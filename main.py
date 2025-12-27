from ingestion import load_documents
from splitter import split_documents
from embeddings import get_embedding_model
from vector_store import create_vector_store
from retriever import retrieve_chunks
from llm_answer import generate_answer
from entity_extractor import extract_facts
from kg_answer import answer_from_kg

# -----------------------------
# PHASE 1: INGESTION
# -----------------------------
documents = load_documents("data")
print(f"Loaded {len(documents)} documents")

# -----------------------------
# PHASE 2: CHUNKING
# -----------------------------
chunks = split_documents(documents)
print(f"Created {len(chunks)} chunks")

# -----------------------------
# PHASE 3: EMBEDDINGS
# -----------------------------
embeddings = get_embedding_model()

# -----------------------------
# PHASE 4: VECTOR STORE
# -----------------------------
vectordb = create_vector_store(chunks, embeddings)
print("Vector store created")
print("vectordb type:", type(vectordb))

# -----------------------------
# STEP 1 (KG): EXTRACT FACTS ONCE
# -----------------------------
facts = extract_facts(documents)
print(f"Extracted {len(facts)} facts from documents")

# -----------------------------
# PHASE 5 & 6: INTERACTIVE KG-RAG LOOP
# -----------------------------
print("\nInteractive KG-RAG mode started")
print("Type 'exit' to quit\n")

while True:
    query = input("Ask a question: ").strip()

    if query.lower() == "exit":
        print("Exiting KG-RAG assistant. Bye!")
        break

    print(f"\nQuery: {query}")

    # 1️⃣ Try Knowledge Graph first
    kg_answer = answer_from_kg(query, facts)
    if kg_answer:
        print("\n--- KG ANSWER ---")
        print(kg_answer)
        print("\n" + "=" * 80 + "\n")
        continue

    # 2️⃣ Fall back to traditional RAG
    retrieved_docs = retrieve_chunks(query, vectordb, k=3)

    final_answer = generate_answer(query, retrieved_docs)

    print("\n--- RAG ANSWER ---")
    print(final_answer)
    print("\n" + "=" * 80 + "\n")
