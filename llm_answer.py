from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import re


def answer_supported_by_context(answer: str, context: str) -> bool:
    """
    Simple hallucination guard:
    Check whether at least some meaningful words from the answer
    appear in the retrieved context.
    """

    # Normalize text
    answer = answer.lower()
    context = context.lower()

    # Remove very common filler words
    stopwords = {
        "the", "is", "was", "and", "or", "to", "of", "in", "a",
        "that", "this", "it", "as", "with", "for", "on", "by"
    }

    # Extract keywords from answer
    answer_words = {
        word for word in re.findall(r"\b[a-z]{4,}\b", answer)
        if word not in stopwords
    }

    if not answer_words:
        return False

    # Count how many answer keywords appear in context
    matches = sum(1 for word in answer_words if word in context)

    # Require at least 2 keyword overlaps (tunable)
    return matches >= 2


def generate_answer(query, retrieved_docs):
    """
    Generate a final answer using Retrieval-Augmented Generation (RAG)
    with hallucination guard.
    """

    # Combine retrieved documents into context
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    system_prompt = """
You are an AI assistant answering questions using Retrieval-Augmented Generation (RAG).

Rules (STRICT):
1. Use ONLY the information explicitly stated in the retrieved context.
2. Do NOT use prior knowledge or assumptions.
3. If the answer is not explicitly present in the context, respond exactly with:
   "I don't know based on the provided documents."
4. Be concise, factual, and accurate.
"""

    user_prompt = f"""
Context:
{context}

Question:
{query}

Answer:
"""

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt),
    ]

    response = llm.invoke(messages)
    answer = response.content.strip()

    # ✅ HALLUCINATION GUARD (THIS IS THE LINE YOU ASKED ABOUT)
    if not answer_supported_by_context(answer, context):
        return "I don't know based on the provided documents."

    return answer
