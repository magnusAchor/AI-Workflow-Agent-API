from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional
from app.utils.llm import call_llm


# =========================
# STATE
# =========================
class AgentState(TypedDict):
    input: str
    article: Optional[str]
    email: Optional[str]
    final_output: Optional[dict]


# =========================
# NODE 1 — WRITE ARTICLE (REAL LLM STEP)
# =========================
def write_node(state: AgentState):
    prompt = f"""
    Write a detailed, well-structured article about:
    {state['input']}
    """

    article = call_llm(prompt)
    state["article"] = article
    return state


# =========================
# NODE 2 — FORMAT EMAIL
# =========================
def format_node(state: AgentState):
    state["email"] = f"Subject: AI Generated Article\n\n{state['article']}"
    return state


# =========================
# NODE 3 — SEND EMAIL (MOCK)
# =========================
def email_node(state: AgentState):
    state["final_output"] = {
        "status": "sent",
        "message": "Email sent successfully (mock)",
        "content": state["email"]
    }
    return state


# =========================
# BUILD GRAPH
# =========================
def build_workflow():
    graph = StateGraph(AgentState)

    graph.add_node("write", write_node)
    graph.add_node("format", format_node)
    graph.add_node("email", email_node)

    graph.set_entry_point("write")

    graph.add_edge("write", "format")
    graph.add_edge("format", "email")
    graph.add_edge("email", END)

    return graph.compile()


workflow = build_workflow()