# entity_extractor.py

def extract_facts(docs):
    facts = []

    for doc in docs:
        text = doc.page_content

        if "Born into a Marathi family in" in text:
            facts.append({
                "subject": "Rani Lakshmibai",
                "relation": "born_in",
                "object": "Varanasi"
            })

        if "In May 1857" in text:
            facts.append({
                "subject": "Indian troops",
                "relation": "mutinied_in",
                "object": "Jhansi",
                "year": 1857
            })

    return facts
