from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional

# =========================
# TOOLS (your real logic)
# =========================
def summarize(text: str) -> str:
    return text.split(".")[0]

def format_message(summary: str) -> str:
    return f"Subject: AI Summary\n\n{summary}"

def send_email(content: str):
    return {
        "status": "sent",
        "message": "Email sent successfully (mock)",
        "content": content
    }


# =========================
# STATE (shared memory)
# =========================
class AgentState(TypedDict):
    input: str
    summary: Optional[str]
    email: Optional[str]
    final_output: Optional[dict]


# =========================
# NODES (WRAPPERS around tools)
# =========================

def summarize_node(state: AgentState):
    text = state["input"]
    state["summary"] = summarize(text)
    return state


def format_node(state: AgentState):
    summary = state["summary"]
    state["email"] = format_message(summary)
    return state


def email_node(state: AgentState):
    email_content = state["email"]
    state["final_output"] = send_email(email_content)
    return state


# =========================
# BUILD GRAPH (ORCHESTRATION)
# =========================

def build_workflow():
    graph = StateGraph(AgentState)

    # register nodes
    graph.add_node("summarize", summarize_node)
    graph.add_node("format", format_node)
    graph.add_node("email", email_node)

    # define flow (this is the "workflow")
    graph.set_entry_point("summarize")

    graph.add_edge("summarize", "format")
    graph.add_edge("format", "email")
    graph.add_edge("email", END)

    return graph.compile()


# =========================
# RUN WORKFLOW
# =========================

workflow = build_workflow()


# Optional test run (you can delete this later)
if __name__ == "__main__":
    result = workflow.invoke({
        "input": "This is a long article. It contains many details about AI systems.",
        "summary": None,
        "email": None,
        "final_output": None
    })

    print(result)