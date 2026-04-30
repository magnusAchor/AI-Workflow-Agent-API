def send_email(content: str) -> dict:
    return {
        "status": "sent",
        "message": "Email successfully simulated",
        "content": content
    }