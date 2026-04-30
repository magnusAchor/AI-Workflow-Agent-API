class PlannerAgent:
    """
    Converts natural language into structured workflow steps
    """

    def create_plan(self, user_input: str):
        text = user_input.lower()

        if "email" in text and "summarize" in text:
            return [
                "summarize",
                "format_email",
                "send_email"
            ]

        if "summarize" in text:
            return ["summarize"]

        return ["summarize"]