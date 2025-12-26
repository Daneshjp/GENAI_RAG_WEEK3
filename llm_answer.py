from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


def generate_answer(query, retrieved_docs):
    """
    Generate a final answer using RAG (retrieved context + LLM)
    """

    # Combine retrieved documents into context
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    system_prompt = (
        "You are a helpful assistant. "
        "Answer the question using ONLY the provided context. "
        "If the answer is not in the context, say you don't know."
    )

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

    return response.content
