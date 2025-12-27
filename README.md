📘 Retrieval-Augmented Question Answering on Class XII English Textbook
Overview

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline built on a Class XII English textbook (PDF). The goal was to answer questions strictly grounded in the provided documents, while preventing hallucinations and unsupported responses.

The system was developed as part of a Gen-AI coursework assignment to understand:

Vector databases

Semantic retrieval

Hallucination risks

Prompt engineering inside RAG

Guardrails for factual accuracy

Why Vanilla RAG Failed Initially

A basic RAG pipeline retrieves semantically similar text and asks an LLM to generate an answer.
However, this can still hallucinate when:

Retrieved chunks are loosely related but not answer-supporting

The LLM fills gaps using general world knowledge

Questions are outside the document scope

Example Failure

When asked:

“What are three ways to fine-tune a language model using this textbook?”

The LLM generated a generic AI answer — even though the textbook contains no such information.

How Hallucination Was Fixed

Two guardrails were implemented:

1️⃣ Strict RAG Prompt

The LLM is explicitly instructed to:

Use only retrieved context

Return “I don’t know based on the provided documents” if unsupported

2️⃣ Post-Generation Validation (Key Fix)

A validation step checks whether the generated answer is actually supported by retrieved context.

If not:

I don't know based on the provided documents.


This prevents:

Out-of-scope answers

Hallucinated explanations

General AI knowledge leakage

Multi-File Ingestion

The ingestion pipeline supports multiple document formats:

📄 PDF (textbook)

📃 TXT

📝 Markdown

📘 DOCX

All files placed in the /data folder are:

Loaded

Chunked

Embedded

Stored in a vector database (Chroma)

This allows scalable document expansion without code changes.

System Architecture
PDF/Text Files
      ↓
Document Loader
      ↓
Text Chunking
      ↓
Embeddings
      ↓
Vector Store (Chroma)
      ↓
Retriever
      ↓
LLM + Guardrails
      ↓
Final Answer or "I don't know"

Example Questions Tested
✅ Factual Question (Success)

Who is the author of “An Astrologer’s Day” and when did he receive the Sahitya Akademi Award?

✔ Correctly answered using document context

✅ Interpretive Question (Success)

Why does the astrologer feel “a great load is gone” at the end?

✔ Answer grounded in the story’s text

❌ Unsupported Question (Correctly Rejected)

How can this textbook be used to fine-tune an LLM for sentiment analysis?

✔ Response:

I don't know based on the provided documents.

Key Learning Outcomes

RAG reduces hallucination but does not eliminate it by default

Prompt engineering alone is not sufficient

Post-generation validation is essential for safety

Vector similarity ≠ factual correctness

Guardrails make RAG production-ready

Future Improvements

Confidence scoring (RAG vs KG)

Sentence-level citation checking

Knowledge Graph visualisation

Agent-based RAG (LangGraph)

UI-based chatbot interface

Tech Stack

Python

LangChain

OpenAI GPT-3.5

Chroma Vector DB

PDF/Text loaders

Author

JP
Gen-AI - RAG chatbot - Assignment
December 2025
