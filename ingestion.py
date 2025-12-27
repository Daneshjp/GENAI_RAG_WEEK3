import os
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredMarkdownLoader,
)

def load_documents(data_dir: str):
    documents = []

    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)

        try:
            # PDF
            if filename.lower().endswith(".pdf"):
                loader = PyPDFLoader(filepath)
                docs = loader.load()
                documents.extend(docs)
                print(f"Loaded {filename} ({len(docs)} pages)")

            # TXT
            elif filename.lower().endswith(".txt"):
                loader = TextLoader(filepath, encoding="utf-8")
                docs = loader.load()
                documents.extend(docs)
                print(f"Loaded {filename} ({len(docs)} pages)")

            # DOCX
            elif filename.lower().endswith(".docx"):
                loader = Docx2txtLoader(filepath)  # ❗ NO encoding
                docs = loader.load()
                documents.extend(docs)
                print(f"Loaded {filename} ({len(docs)} pages)")

            # MARKDOWN
            elif filename.lower().endswith(".md"):
                loader = UnstructuredMarkdownLoader(filepath)
                docs = loader.load()
                documents.extend(docs)
                print(f"Loaded {filename} ({len(docs)} pages)")

            else:
                print(f"Skipped unsupported file: {filename}")

        except Exception as e:
            print(f"Failed to load {filename}: {e}")

    return documents
