from app.tools.summarizer import summarize
from app.tools.formatter import format_message
from app.tools.emailer import send_email
from app.tools.logger import log_step

class ExecutorAgent:

    async def execute(self, plan, user_input):
        tool_calls = []
        state = {"text": user_input, "summary": None, "email": None}

        for step in plan:
            try:
                if step == "summarize":
                    output = summarize(state["text"])
                    state["summary"] = output

                elif step == "format_email":
                    output = format_message(state["summary"])
                    state["email"] = output

                elif step == "send_email":
                    output = send_email(state["email"])

                log_step(step, output)

                tool_calls.append({
                    "tool": step,
                    "input": state,
                    "output": output
                })

            except Exception as e:
                tool_calls.append({
                    "tool": step,
                    "error": str(e)
                })

        return {
            "tool_calls": tool_calls,
            "final_output": tool_calls[-1]["output"] if tool_calls else None
        }