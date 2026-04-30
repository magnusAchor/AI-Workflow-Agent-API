from typing import TypedDict, Optional

class AgentState(TypedDict):
    input: str
    summary: Optional[str]
    email: Optional[str]
    final_output: Optional[str]