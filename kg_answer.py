def answer_from_kg(question, facts):
    q = question.lower()

    for fact in facts:
        if "where" in q and "born" in q:
            if fact["relation"] == "born_in":
                return f'{fact["subject"]} was born in {fact["object"]}.'

        if "which year" in q or "when" in q:
            if fact.get("year"):
                return f'The event happened in {fact["year"]}.'

    return None
