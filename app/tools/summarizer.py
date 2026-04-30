def summarize(text: str) -> str:
    # lightweight mock summarizer (replace with OpenAI if needed)
    sentences = text.split(".")
    return sentences[0] if sentences else text