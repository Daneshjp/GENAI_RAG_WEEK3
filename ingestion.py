from langchain_community.document_loaders import PyPDFLoader
import os


def load_documents(data_dir: str):
    documents = []

    for file in os.listdir(data_dir):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(data_dir, file))
            documents.extend(loader.load())

    return documents
